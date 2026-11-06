#!/usr/bin/env python3
"""Test 1 runner with loop protection.

Uses the streaming guard: aborts a response that repeats the same 8-word
shingle more than N times, applies a 15-minute timeout and a low temperature.

Usage:
  python3 run_chains_guarded.py --dataset dataset_20k.json --model local-only \
      --max-tokens 65535 --timeout 900 --temp 0.3 --out results_next_chains_guarded.json
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard import ask_guarded


def parse_int(text):
    m = re.search(r"-?\d+", (text or "").replace("−", "-"))
    return int(m.group(0)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--max-tokens", type=int, default=65535)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--temp", type=float, default=0.3)
    ap.add_argument("--fp", type=float, default=0.3)
    ap.add_argument("--pp", type=float, default=0.3)
    ap.add_argument("--ids", default="")
    ap.add_argument("--resume", action="store_true", help="continue an existing result file")
    ap.add_argument("--force", action="store_true", help="overwrite an existing result file")
    ap.add_argument("--out", default="chains_guarded.json")
    a = ap.parse_args()
    if os.path.exists(a.out) and not a.force and not a.resume:
        raise SystemExit("refusing to overwrite %s (use --force to replace)" % a.out)
    TEMP_DEFAULT = None if a.temp < 0 else a.temp

    done_rows = []
    done_ids = set()
    if a.resume and os.path.exists(a.out):
        prev = json.load(open(a.out))
        done_rows = prev.get("rows") or []
        # a task that hit the length cap is not done: retry it with the larger budget
        done_ids = {str(r.get("id")) for r in done_rows if r.get("finish") != "length"}
    d = json.load(open(a.dataset))
    tasks = d["tasks"]
    if done_ids:
        tasks = [t for t in tasks if str(t["id"]) not in done_ids]
    if a.ids:
        want = {int(x) for x in a.ids.split(",") if x.strip()}
        tasks = [t for t in tasks if t["id"] in want]
    print("dataset: %s | model: %s | tasks: %d | max_tokens: %d | timeout: %d s | temp: %.2f"
          % (a.dataset, a.model, len(tasks), a.max_tokens, a.timeout, a.temp), flush=True)

    rows = list(done_rows)
    for t in tasks:
        if os.path.exists(os.environ.get("CHAIN_BENCH_PAUSE_FILE", "PAUSE")):
            print("\npaused: pause file present, remaining tasks kept for --resume", flush=True)
            break
        prompt = d["document"] + "\n\nВопрос: " + t["question"]
        for _attempt in range(3):
            out = ask_guarded(prompt, a.model, max_tokens=a.max_tokens,
                              timeout=a.timeout, temperature=TEMP_DEFAULT,
                              frequency_penalty=a.fp, presence_penalty=a.pp)
            if not out.get("stalled"):
                break
            print("  stall detected, retrying (%d/3)" % (_attempt + 1), flush=True)
        if "answer" not in t:
            raise SystemExit("schema error: task %s has no answer field" % t.get("id"))
        got = parse_int(out.get("content"))
        ok = (got == t["answer"])
        kind = "ok" if ok else ("loop" if out.get("loop") else
                                ("timeout" if out.get("timeout") else
                                 ("error" if out.get("error") else "wrong")))
        rows.append({"id": t["id"], "answer": t["answer"], "got": got, "ok": ok,
                     "kind": kind, "latency_s": round(out.get("latency", 0), 1),
                     "finish": out.get("finish"), "error": out.get("error"),
                     "raw": (out.get("content") or "")[:20000],
                     "raw_tail": (out.get("content") or "")[-400:],
                     "server_timings": out.get("timings")})
        _st = out.get("timings") or {}
        _sp = ""
        if isinstance(_st, dict) and _st.get("predicted_per_second"):
            _sp = " | gen %.1f t/s (%d tok) | prefill %.0f t/s" % (
                _st["predicted_per_second"], _st.get("predicted_n", 0),
                _st.get("prompt_per_second") or 0)
        print("  %2d | expected %5d | got %s | %-7s | %6.1f c%s"
              % (t["id"], t["answer"], ("%5d" % got) if got is not None else "    —",
                 kind, out.get("latency", 0), _sp), flush=True)

    errors = [r for r in rows if r.get("kind") == "error"]
    if errors:
        # the route changed under us or the model was unloaded: keep nothing
        out_failed = a.out.replace(".json", ".failed.json")
        json.dump({"dataset": a.dataset, "model": a.model, "max_tokens": a.max_tokens,
                   "temperature": a.temp, "aborted": True, "errors": len(errors), "rows": rows},
                  open(out_failed, "w"), ensure_ascii=False, indent=1)
        print("\nabort_transport: %d/%d requests failed (%s) -> %s; result discarded"
              % (len(errors), len(rows), errors[0].get("error"), out_failed))
        sys.exit(2)

    ok_n = sum(1 for r in rows if r["ok"])
    loops = sum(1 for r in rows if r["kind"] == "loop")
    print("\nTOTAL: %d/%d correct (%.0f%% errors) | loops: %d"
          % (ok_n, len(rows), 100.0 * (len(rows) - ok_n) / len(rows), loops))
    json.dump({"dataset": a.dataset, "model": a.model, "max_tokens": a.max_tokens,
               "temperature": a.temp, "rows": rows}, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("file:", a.out)


if __name__ == "__main__":
    main()
