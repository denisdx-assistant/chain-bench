#!/usr/bin/env python3
"""Frozen programs replay with loop protection and incremental saving.

Same inputs as run_frozen.py, but each request goes through the streaming
guard (repetition detection + timeout), applies temperature/penalties, and the
result file is rewritten after every program so an interrupted run keeps
finished work.

Usage:
  python3 run_frozen_guarded.py --dir datasets/programs/v4 --model local-only \
      --max-tokens 32000 --timeout 900 --temp 0.3 --fp 0.3 --pp 0.3 \
      --out results/programs_next_guarded.json
"""
import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard import ask_guarded

QUESTION = ("\n\nQuestion: name the final array arr after running this program and its sum. "
            "Answer strictly as:\nARRAY: [numbers, comma separated]\nSUM: number")


def parse_array(text):
    m = re.search(r'ARRAY:\s*\[([^\]]*)\]', text or '')
    if not m:
        return None
    nums = [int(x) for x in re.findall(r'-?\d+', m.group(1))]
    return nums if len(nums) == 10 else None


def parse_sum(text):
    m = re.search(r'SUM:\s*(-?\d+)', text or '')
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--temp", type=float, default=0.3)
    ap.add_argument("--fp", type=float, default=0.3)
    ap.add_argument("--pp", type=float, default=0.3)
    ap.add_argument("--only", default="", help="comma list of program stems")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.dir, "*.py")))
    if a.only:
        want = {x.strip() for x in a.only.split(",") if x.strip()}
        files = [f for f in files if os.path.splitext(os.path.basename(f))[0] in want]
    print("dir: %s | model: %s | programs: %d | max_tokens: %d | timeout: %d s | temp: %.2f"
          % (a.dir, a.model, len(files), a.max_tokens, a.timeout, a.temp), flush=True)

    rows = []
    for path in files:
        stem = os.path.splitext(path)[0]
        code = open(path).read()
        try:
            exp = json.load(open(stem + ".json"))
        except Exception:
            print("  %s | нет ожидаемого json, пропуск" % os.path.basename(path), flush=True)
            continue
        out = ask_guarded(code + QUESTION, a.model, max_tokens=a.max_tokens,
                          timeout=a.timeout, temperature=a.temp,
                          frequency_penalty=a.fp, presence_penalty=a.pp,
                          client='openclaw-frozen-guard')
        got_arr = parse_array(out.get("content"))
        got_sum = parse_sum(out.get("content"))
        ok_arr = got_arr == exp.get("array")
        ok_sum = got_sum == exp.get("sum")
        ok = bool(ok_arr and ok_sum)
        kind = "ok" if ok else ("loop" if out.get("loop") else
                                ("timeout" if out.get("timeout") else
                                 ("error" if out.get("error") else "wrong")))
        rows.append({"file": os.path.basename(path), "ok": ok, "kind": kind,
                     "arr_ok": ok_arr, "sum_ok": ok_sum,
                     "latency_s": round(out.get("latency", 0), 1),
                     "finish": out.get("finish"),
                     "reasoning_chars": out.get("reasoning_chars"),
                     "error": out.get("error")})
        print("  %-22s | %-7s | arr %s | sum %s | %6.1f c"
              % (os.path.basename(path), kind, "ok" if ok_arr else "no",
                 "ok" if ok_sum else "no", out.get("latency", 0)), flush=True)
        json.dump({"dir": a.dir, "model": a.model, "max_tokens": a.max_tokens,
                   "temperature": a.temp, "frequency_penalty": a.fp,
                   "presence_penalty": a.pp, "rows": rows},
                  open(a.out, "w"), ensure_ascii=False, indent=1)

    ok_n = sum(1 for r in rows if r["ok"])
    loops = sum(1 for r in rows if r["kind"] == "loop")
    print("\nTOTAL: %d/%d correct (%.0f%% errors) | loops: %d"
          % (ok_n, len(rows), 100.0 * (len(rows) - ok_n) / max(len(rows), 1), loops))
    print("file:", a.out)


if __name__ == "__main__":
    main()
