#!/usr/bin/env python3
"""Test 1 runner, three clients at a time.

The sequential runner measures one stream. This one keeps `--workers` requests in flight
so a server with continuous batching is actually forced to batch, and records what that
does to prefill and generation.

Two numbers matter here and they are not the same:

- the per-request `predicted_per_second` the server reports, which falls when requests
  share the GPU;
- the aggregate throughput, total tokens written divided by the wall time of the batch,
  which can rise even while every individual stream gets slower.

Rows carry `start_ts`/`end_ts` and the number of other requests that overlapped them, so
the analysis never has to guess whether batching happened.

Usage:
  python3 run_chains_parallel.py --dataset datasets/chains/zh/dataset_20k_17tasks.json \
      --model qwen3.8-flash-next-abiray-coder-iq1_m --workers 3 \
      --max-tokens 32000 --out results/M/chains_zh_20k_32k_par3.json
"""
import argparse
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard import ask_guarded
from run_chains_guarded import _dump_raw, parse_int


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--temp", type=float, default=-1)
    ap.add_argument("--fp", type=float, default=0.2)
    ap.add_argument("--pp", type=float, default=0.2)
    ap.add_argument("--limit", type=int, default=0, help="run only the first N tasks")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    if os.path.exists(a.out) and not a.force:
        raise SystemExit("refusing to overwrite %s (use --force)" % a.out)

    TEMP_DEFAULT = None if a.temp < 0 else a.temp
    d = json.load(open(a.dataset))
    tasks = d["tasks"][: a.limit] if a.limit else list(d["tasks"])
    print("dataset: %s | model: %s | tasks: %d | workers: %d | max_tokens: %d"
          % (a.dataset, a.model, len(tasks), a.workers, a.max_tokens), flush=True)
    if a.dry_run:
        for t in tasks[:5]:
            print("  would run task %s" % t.get("id"))
        return

    rows, lock = [], threading.Lock()
    t_zero = time.time()

    def run_task(t):
        prompt = d["document"] + "\n\nВопрос: " + t["question"]
        start = time.time()
        out = ask_guarded(prompt, a.model, max_tokens=a.max_tokens, timeout=a.timeout,
                          temperature=TEMP_DEFAULT, frequency_penalty=a.fp,
                          presence_penalty=a.pp)
        end = time.time()
        got = parse_int(out.get("content"))
        ok = (got == t["answer"])
        kind = "ok" if ok else ("loop" if out.get("loop") else
                                ("timeout" if out.get("timeout") else
                                 ("error" if out.get("error") else "wrong")))
        row = {"id": t["id"], "answer": t["answer"], "got": got, "ok": ok, "kind": kind,
               "latency_s": round(end - start, 1), "start_ts": round(start - t_zero, 2),
               "end_ts": round(end - t_zero, 2), "finish": out.get("finish"),
               "error": out.get("error"),
               "raw_tail": (out.get("content") or "")[-400:],
               "server_timings": out.get("timings")}
        with lock:
            rows.append(row)
            _dump_raw(a.out, t["id"], out.get("content") or "", out.get("reasoning_text") or "")
            st = out.get("timings") or {}
            sp = ""
            if isinstance(st, dict) and st.get("predicted_per_second"):
                sp = " | gen %.1f t/s (%d tok) | prefill %.0f t/s" % (
                    st["predicted_per_second"], st.get("predicted_n", 0),
                    st.get("prompt_per_second") or 0)
            print("  %2s | expected %5s | got %5s | %-7s | %6.1f c%s"
                  % (t["id"], t["answer"], got if got is not None else "—",
                     kind, end - start, sp), flush=True)
            tmp = a.out + ".tmp"
            json.dump({"dataset": a.dataset, "model": a.model, "max_tokens": a.max_tokens,
                       "workers": a.workers, "rows": rows}, open(tmp, "w"),
                      ensure_ascii=False, indent=1)
            os.replace(tmp, a.out)

    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        list(pool.map(run_task, tasks))

    # how many other requests were in flight during each task
    for r in rows:
        peers = 0
        for o in rows:
            if o is r:
                continue
            if o["start_ts"] < r["end_ts"] and r["start_ts"] < o["end_ts"]:
                peers += 1
        r["concurrent_peers"] = peers

    wall = max(r["end_ts"] for r in rows) - min(r["start_ts"] for r in rows)
    toks = sum((r.get("server_timings") or {}).get("predicted_n") or 0 for r in rows)
    ok_n = sum(1 for r in rows if r["ok"])
    summary = {"workers": a.workers, "tasks": len(rows), "correct": ok_n,
               "wall_s": round(wall, 1),
               "tasks_per_min": round(60.0 * len(rows) / wall, 2) if wall else None,
               "aggregate_gen_tps": round(toks / wall, 1) if wall else None,
               "solo_rows": sum(1 for r in rows if r["concurrent_peers"] == 0),
               "batched_rows": sum(1 for r in rows if r["concurrent_peers"] > 0)}
    print("\nTOTAL: %d/%d correct | wall %.0f s | %.2f tasks/min | aggregate %.1f tok/s | "
          "rows alone %d, rows batched %d"
          % (ok_n, len(rows), wall, summary["tasks_per_min"], summary["aggregate_gen_tps"],
             summary["solo_rows"], summary["batched_rows"]))
    json.dump({"dataset": a.dataset, "model": a.model, "max_tokens": a.max_tokens,
               "workers": a.workers, "summary": summary, "rows": rows},
              open(a.out, "w"), ensure_ascii=False, indent=1)
    print("file:", a.out)


if __name__ == "__main__":
    main()
