#!/usr/bin/env python3
"""Guarded streaming call: abort on degenerate repetition.

The model sometimes enters a loop, repeating the same noise block. A plain
max_tokens limit does not help: the answer never arrives, the budget is spent
on repeats. This wrapper streams the response, counts 8-word shingles, and
closes the connection once one shingle repeats more than `max_repeat` times.

Returns a dict with `loop: True` when aborted, plus partial content.
"""
import json
import os
import re
import os
import time
import urllib.error
import urllib.request
import threading

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "endpoint")
BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or (open(_cfg).read().strip() if os.path.exists(_cfg) else "")
        or "http://127.0.0.1:21434")


def _shingles(text, n=8):
    words = re.findall(r"\w+", text.lower())
    return set(tuple(words[i:i + n]) for i in range(len(words) - n + 1))


def _loop_repeats(text, n=8, window=8000):
    """How often the most repeated 8-word phrase occurs inside the recent tail.

    Counting over the whole stream is wrong: a long reasoning trace reuses stock
    phrases naturally and eventually crosses any fixed threshold. A loop shows up
    as dense repetition *inside a short window*.
    """
    words = re.findall(r"\w+", text[-window:].lower())
    if len(words) < n * 4:
        return 0
    counts = {}
    for i in range(len(words) - n + 1):
        sh = tuple(words[i:i + n])
        counts[sh] = counts.get(sh, 0) + 1
    return max(counts.values()) if counts else 0


def _watch_queue(base, model, stop, stall):
    """Detect a request the server no longer knows about."""
    import threading
    url = base + "/v1/models/" + model + "/queue-state"
    zero = 0
    while not stop.is_set():
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                q = json.load(r) or {}
            active = q.get("active_count")
            loaded = q.get("model_loaded")
            if loaded is False:
                zero = 0          # still loading: an idle counter means nothing yet
            elif active == 0:
                zero += 1
                if zero >= 2:
                    stall.set()
                    return
            else:
                zero = 0
        except Exception:
            pass
        time.sleep(20)


def _queue_depth(base, model):
    try:
        with urllib.request.urlopen(base + "/v1/models/" + model + "/queue-state", timeout=10) as r:
            d = json.loads(r.read())
        return int(d.get("queued_count_total") or 0)
    except Exception:
        return 0


def wait_for_queue(base, model, max_wait=900, step=60, log=print):
    """Yield the single model slot to other clients before sending a benchmark request.

    The server admits one request at a time, so a benchmark task holds the GPU for
    minutes. Waiting until the queue is empty keeps OpenClaw's own calls from
    timing out behind us. Set CHAIN_BENCH_POLITE=0 to send regardless.
    """
    if os.environ.get("CHAIN_BENCH_POLITE", "1") == "0":
        return 0
    waited = 0
    while waited < max_wait:
        depth = _queue_depth(base, model)
        if depth == 0:
            return waited
        log("  %d other request(s) waiting, yielding %ds to them" % (depth, step))
        time.sleep(step)
        waited += step
    return waited

def ask_guarded(prompt, model, max_tokens=65535, timeout=900, temperature=0.3,
                max_repeat=12, threshold_n=8, client='chain-bench', frequency_penalty=0.0, presence_penalty=0.0):
    payload = {"model": model, "max_tokens": max_tokens, "stream": True}
    if temperature is not None:
        payload["temperature"] = temperature
    if frequency_penalty:
        payload["frequency_penalty"] = frequency_penalty
    if presence_penalty:
        payload["presence_penalty"] = presence_penalty
    payload["messages"] = [{"role": "user", "content": prompt}]
    wait_for_queue(BASE, model)
    body = json.dumps(payload).encode()
    req = urllib.request.Request(BASE + '/v1/chat/completions', data=body,
                                 headers={'Content-Type': 'application/json',
                                          'X-Aidir-Client': client})
    t0 = time.time()
    content = []
    reasoning = []
    timings = None
    usage = None
    finish = None
    counts = {}
    checked_at = 0
    r = None
    for attempt in range(1, 4):
        try:
            r = urllib.request.urlopen(req, timeout=timeout)
            break
        except urllib.error.HTTPError as e:
            if e.code >= 500 and attempt < 3:
                time.sleep(15)
                continue
            return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
        except Exception as e:
            if attempt < 3:
                time.sleep(15)
                continue
            return {"error": str(e)[:150], "latency": time.time() - t0}
    stop = threading.Event()
    stall = threading.Event()
    if os.environ.get("CHAIN_BENCH_WATCH") == "1":
        threading.Thread(target=_watch_queue, args=(BASE, model, stop, stall), daemon=True).start()
    try:
        _sock = getattr(getattr(getattr(r, "fp", None), "raw", None), "_sock", None)
        if _sock is not None:
            _sock.settimeout(30)
    except Exception:
        pass
    try:
        while True:
            try:
                raw = r.readline()
            except Exception as exc:
                msg = str(exc).lower()
                if "timed out" in msg or isinstance(exc, TimeoutError):
                    if stall.is_set():
                        stop.set()
                        try: r.close()
                        except Exception: pass
                        return {"content": ''.join(content), "loop": False, "timeout": False,
                                "stalled": True, "latency": time.time() - t0, "finish": "stalled"}
                    if time.time() - t0 > timeout:
                        r.close()
                        return {"content": ''.join(content), "loop": False, "timeout": True,
                                "latency": time.time() - t0, "finish": "timeout"}
                    continue
                return {"error": str(exc)[:150], "latency": time.time() - t0}
            if not raw:
                break
            if time.time() - t0 > timeout:
                r.close()
                return {"content": ''.join(content), "loop": False,
                        "timeout": True, "latency": time.time() - t0, "finish": "timeout"}
            line = raw.decode('utf-8', 'replace').strip()
            if not line.startswith('data:'):
                continue
            data = line[5:].strip()
            if data == '[DONE]':
                break
            try:
                obj = json.loads(data)
            except Exception:
                continue
            if obj.get('timings'):
                timings = obj['timings']
            if obj.get('usage'):
                usage = obj['usage']
            ch = (obj.get('choices') or [{}])[0]
            delta = ch.get('delta') or {}
            if delta.get('content'):
                content.append(delta['content'])
            if delta.get('reasoning_content'):
                reasoning.append(delta['reasoning_content'])
            if ch.get('finish_reason'):
                finish = ch['finish_reason']

            joined = ''.join(content) + ''.join(reasoning)
            if len(joined) - checked_at > 4000:
                checked_at = len(joined)
                if _loop_repeats(joined, threshold_n) >= max_repeat:
                    r.close()
                    return {"content": ''.join(content), "loop": True, "timeout": False,
                            "latency": time.time() - t0, "finish": "loop",
                            "timings": timings, "usage": usage,
                            "reasoning_chars": len(''.join(reasoning)),
                            "reasoning_tail": ''.join(reasoning)[-2000:]}
    except urllib.error.HTTPError as e:
        return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
    except Exception as e:
        return {"error": str(e)[:150], "latency": time.time() - t0}

    _joined = ''.join(content) + ''.join(reasoning)
    return {"content": ''.join(content), "loop": False, "timeout": False,
            "latency": time.time() - t0, "finish": finish,
            "timings": timings, "usage": usage,
            "reasoning_chars": len(''.join(reasoning)),
            "reasoning_tail": ''.join(reasoning)[-2000:],
            "repeat_max": _loop_repeats(_joined)}
