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
import time
import urllib.error
import urllib.request

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "endpoint")
BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or (open(_cfg).read().strip() if os.path.exists(_cfg) else "")
        or "http://127.0.0.1:21434")


def _shingles(text, n=8):
    words = re.findall(r"\w+", text.lower())
    return set(tuple(words[i:i + n]) for i in range(len(words) - n + 1))


def ask_guarded(prompt, model, max_tokens=65535, timeout=900, temperature=0.3,
                max_repeat=40, client='openclaw-guard', frequency_penalty=0.0, presence_penalty=0.0):
    payload = {"model": model, "max_tokens": max_tokens, "stream": True}
    if temperature is not None:
        payload["temperature"] = temperature
    if frequency_penalty:
        payload["frequency_penalty"] = frequency_penalty
    if presence_penalty:
        payload["presence_penalty"] = presence_penalty
    payload["messages"] = [{"role": "user", "content": prompt}]
    body = json.dumps(payload).encode()
    req = urllib.request.Request(BASE + '/v1/chat/completions', data=body,
                                 headers={'Content-Type': 'application/json',
                                          'X-Aidir-Client': client})
    t0 = time.time()
    content = []
    reasoning = []
    finish = None
    counts = {}
    checked_at = 0
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        for raw in r:
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
                for sh in _shingles(joined):
                    counts[sh] = counts.get(sh, 0) + 1
                if counts and max(counts.values()) > max_repeat:
                    r.close()
                    return {"content": ''.join(content), "loop": True, "timeout": False,
                            "latency": time.time() - t0, "finish": "loop",
                            "reasoning_chars": len(''.join(reasoning))}
    except urllib.error.HTTPError as e:
        return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
    except Exception as e:
        return {"error": str(e)[:150], "latency": time.time() - t0}

    return {"content": ''.join(content), "loop": False, "timeout": False,
            "latency": time.time() - t0, "finish": finish,
            "reasoning_chars": len(''.join(reasoning))}
