#!/usr/bin/env python3
"""Send several large prompts at the same time and measure what batching does.

Per-request numbers come from the server's own timings; the aggregate is what matters when
a server batches: total tokens written divided by the wall time of the whole batch. Rows
carry start/end stamps and the number of requests that overlapped them, so "was it really
batched" is a fact in the data, not an assumption.

Usage:
  python3 probe_parallel.py --model local-only --label Qwen3.8-27b-Q6_K_XL \
      --size 250k --workers 2 --max-tokens 8000 --out-dir results/_speed_uniq
"""
import argparse
import json
import os
import statistics
import sys
import threading
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from speed_probe import build_prompt, looks_like_echo

BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "config", "endpoint")).read().strip())


def parse_size(text):
    text = str(text).strip().lower()
    if text.endswith("k"):
        return int(float(text[:-1]) * 1000)
    return int(text)


def ask(prompt, model, max_tokens, timeout=3600):
    payload = {"model": model, "max_tokens": max_tokens, "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(BASE + "/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.load(r)
    return data, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--label", required=True)
    ap.add_argument("--size", default="250k")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--out-dir", default="results/_speed_uniq")
    a = ap.parse_args()

    target = parse_size(a.size)
    rows, lock = [], threading.Lock()
    zero = time.time()

    def worker(i):
        prompt, info = build_prompt(target, a.max_tokens)
        start = time.time() - zero
        try:
            data, wall = ask(prompt, a.model, a.max_tokens)
        except Exception as exc:  # noqa: BLE001 - report, do not crash the batch
            with lock:
                rows.append({"want": target, "worker": i, "error": str(exc)[:160],
                             "start_ts": round(start, 2), "end_ts": round(time.time() - zero, 2)})
            return
        end = time.time() - zero
        st = data.get("timings") or {}
        msg = ((data.get("choices") or [{}])[0].get("message") or {})
        rec = {"want": target, "worker": i,
               "prompt_n": st.get("prompt_n"), "cache_n": st.get("cache_n"),
               "prompt_tps": st.get("prompt_per_second"),
               "gen_tps": st.get("predicted_per_second"),
               "predicted_n": st.get("predicted_n"),
               "finish": (data.get("choices") or [{}])[0].get("finish_reason"),
               "wall_s": round(wall, 1), "start_ts": round(start, 2), "end_ts": round(end, 2),
               "concurrent": True,
               "echo": looks_like_echo(msg.get("content") or ""),
               "story_head": (msg.get("content") or "")[:120].replace("\n", " ")}
        with lock:
            rows.append(rec)
            print("  поток %d: префилл %s t/s, генерация %s t/s, промпт %s, %s c"
                  % (i, round(rec["prompt_tps"] or 0), round(rec["gen_tps"] or 0),
                     rec["prompt_n"], rec["wall_s"]), flush=True)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(a.workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ok = [r for r in rows if not r.get("error") and r.get("prompt_n")]
    wall = max(r["end_ts"] for r in rows) - min(r["start_ts"] for r in rows)
    prompt_tok = sum(r.get("prompt_n") or 0 for r in ok)
    gen_tok = sum(r.get("predicted_n") or 0 for r in ok)
    summary = {"workers": a.workers, "size": target, "requests": len(rows),
               "wall_s": round(wall, 1),
               "aggregate_prefill_tps": round(prompt_tok / wall, 1) if wall and prompt_tok else None,
               "aggregate_gen_tps": round(gen_tok / wall, 1) if wall and gen_tok else None,
               "per_request_prefill": [round(r.get("prompt_tps") or 0) for r in ok],
               "per_request_gen": [round(r.get("gen_tps") or 0) for r in ok],
               "median_gen": round(statistics.median([r["gen_tps"] for r in ok]), 1) if ok else None}
    os.makedirs(a.out_dir, exist_ok=True)
    out = os.path.join(a.out_dir, "%s.json" % a.label)
    prev = []
    if os.path.exists(out):
        try:
            prev = json.load(open(out))
        except Exception:
            prev = []
    tag = "parallel%d" % a.workers
    for r in rows:
        r["mode"] = tag
    merged = [x for x in prev if x.get("mode") != tag] + rows
    json.dump(merged, open(out, "w"), ensure_ascii=False, indent=1)
    print("\nИТОГ: %d потоков, стена %.0f c, суммарный префилл %.0f t/s, суммарная генерация %.1f t/s"
          % (a.workers, wall, summary["aggregate_prefill_tps"] or 0, summary["aggregate_gen_tps"] or 0))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
