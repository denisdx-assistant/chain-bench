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
    ap.add_argument("--out", default="chains_guarded.json")
    a = ap.parse_args()
    TEMP_DEFAULT = None if a.temp < 0 else a.temp

    d = json.load(open(a.dataset))
    tasks = d["tasks"]
    if a.ids:
        want = {int(x) for x in a.ids.split(",") if x.strip()}
        tasks = [t for t in tasks if t["id"] in want]
    print("dataset: %s | model: %s | tasks: %d | max_tokens: %d | timeout: %d s | temp: %.2f"
          % (a.dataset, a.model, len(tasks), a.max_tokens, a.timeout, a.temp), flush=True)

    rows = []
    for t in tasks:
        prompt = d["document"] + "\n\nВопрос: " + t["question"]
        out = ask_guarded(prompt, a.model, max_tokens=a.max_tokens,
                          timeout=a.timeout, temperature=TEMP_DEFAULT,
                          frequency_penalty=a.fp, presence_penalty=a.pp)
        got = parse_int(out.get("content"))
        ok = (got == t["answer"])
        kind = "ok" if ok else ("loop" if out.get("loop") else
                                ("timeout" if out.get("timeout") else
                                 ("error" if out.get("error") else "wrong")))
        rows.append({"id": t["id"], "answer": t["answer"], "got": got, "ok": ok,
                     "kind": kind, "latency_s": round(out.get("latency", 0), 1),
                     "finish": out.get("finish"), "error": out.get("error")})
        print("  %2d | expected %5d | got %s | %-7s | %6.1f c"
              % (t["id"], t["answer"], ("%5d" % got) if got is not None else "    —",
                 kind, out.get("latency", 0)), flush=True)

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
