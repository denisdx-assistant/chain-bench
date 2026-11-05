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
import urllib.request

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "endpoint")
BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or (open(_cfg).read().strip() if os.path.exists(_cfg) else "")
        or "http://127.0.0.1:21434")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard import ask_guarded

QUESTION = ("\n\nQuestion: name the final array arr after running this program and its sum. "
            "Answer strictly as:\nARRAY: [numbers, comma separated]\nSUM: number")


def fetch_meta(model):
    """Provenance: which concrete model/provider the router resolved."""
    try:
        with urllib.request.urlopen(BASE + '/v1/models/' + model, timeout=10) as r:
            d = json.load(r)
        a = d.get('aidir') or {}
        return {"resolved_provider": a.get("resolved_provider"),
                "resolved_model": a.get("resolved_model")}
    except Exception as e:
        return {"resolved_provider": None, "resolved_model": None, "meta_error": str(e)[:120]}


def parse_array(text):
    """Accept the requested format and obvious variants; the last valid list wins."""
    text = text or ''
    candidates = []
    m = re.search(r'ARRAY:\s*\[([^\]]*)\]', text, re.I)
    if m:
        candidates.append(m.group(1))
    for m in re.finditer(r'\[([^\[\]]{0,200})\]', text):
        candidates.append(m.group(1))
    for body in reversed(candidates):
        nums = [int(x) for x in re.findall(r'-?\d+', body)]
        if len(nums) == 10:
            return nums
    return None


def parse_sum(text):
    text = text or ''
    patterns = [r'SUM:\s*(-?\d+)', r'\bsum\b[^0-9\-]{0,20}(-?\d+)',
                r'\btotal\b[^0-9\-]{0,20}(-?\d+)']
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            return int(m.group(1))
    return None


def expected_of(exp):
    """Read the expected answer from either schema; raise if neither is present."""
    arr = exp.get("expected_array", exp.get("array"))
    tot = exp.get("expected_sum", exp.get("sum"))
    if arr is None or tot is None:
        raise ValueError("dataset has no expected_array/expected_sum")
    if isinstance(arr, str):
        arr = json.loads(arr.replace("'", '"'))
    return arr, tot


def score_program(exp, content):
    """Score one answer. Returns (ok, ok_array, ok_sum, got_array, got_sum)."""
    exp_arr, exp_sum = expected_of(exp)
    got_arr, got_sum = parse_array(content), parse_sum(content)
    ok_arr = got_arr is not None and got_arr == exp_arr
    ok_sum = got_sum is not None and got_sum == exp_sum
    return (ok_arr and ok_sum), ok_arr, ok_sum, got_arr, got_sum


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
    ap.add_argument("--force", action="store_true", help="overwrite an existing result file")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if os.path.exists(a.out) and not a.force:
        raise SystemExit("refusing to overwrite %s (use --force to replace)" % a.out)
    TEMP_DEFAULT = None if a.temp < 0 else a.temp

    meta = fetch_meta(a.model)
    files = sorted(glob.glob(os.path.join(a.dir, "*.py")))
    if a.only:
        want = {x.strip() for x in a.only.split(",") if x.strip()}
        files = [f for f in files if os.path.splitext(os.path.basename(f))[0] in want]
    print("resolved: %s / %s" % (meta.get("resolved_provider"), meta.get("resolved_model")), flush=True)
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
        if "expected_array" not in exp and "array" not in exp:
            raise SystemExit("schema error in %s: expected_array/array missing; refusing to score"
                             % os.path.basename(stem))
        out = ask_guarded(code + QUESTION, a.model, max_tokens=a.max_tokens,
                          timeout=a.timeout, temperature=TEMP_DEFAULT,
                          frequency_penalty=a.fp, presence_penalty=a.pp,
                          client='openclaw-frozen-guard')
        got_arr = parse_array(out.get("content"))
        got_sum = parse_sum(out.get("content"))
        # a missing answer must never compare equal to a missing expectation
        if out.get("error"):
            ok, ok_arr, ok_sum, got_arr, got_sum = False, False, False, None, None
        else:
            ok, ok_arr, ok_sum, got_arr, got_sum = score_program(exp, out.get("content") or "")
        kind = "ok" if ok else ("loop" if out.get("loop") else
                                ("timeout" if out.get("timeout") else
                                 ("error" if out.get("error") else "wrong")))
        rows.append({"file": os.path.basename(path), "ok": ok, "kind": kind,
                     "arr_ok": ok_arr, "sum_ok": ok_sum,
                     "latency_s": round(out.get("latency", 0), 1),
                     "finish": out.get("finish"),
                     "reasoning_chars": out.get("reasoning_chars"),
                     "raw": (out.get("content") or "")[:20000],
                     "raw_tail": (out.get("content") or "")[-800:],
                     "server_timings": out.get("timings"),
                     "usage": out.get("usage"),
                     "expected_array": exp.get("expected_array", exp.get("array")),
                     "expected_sum": exp.get("expected_sum", exp.get("sum")),
                     "error": out.get("error")})
        st = out.get("timings") or {}
        speed = ""
        if isinstance(st, dict) and st.get("predicted_per_second"):
            speed = " | gen %.1f t/s (%d tok, %.1fs) | prefill %.0f t/s (%d tok)" % (
                st["predicted_per_second"], st.get("predicted_n", 0),
                (st.get("predicted_ms") or 0) / 1000.0,
                st.get("prompt_per_second") or 0,
                (st.get("prompt_n") or 0) + (st.get("cache_n") or 0))
        print("  %-22s | %-7s | arr %s | sum %s | %6.1f c%s"
              % (os.path.basename(path), kind, "ok" if ok_arr else "no",
                 "ok" if ok_sum else "no", out.get("latency", 0), speed), flush=True)
        json.dump({"dir": a.dir, "model": a.model,
                   "resolved_provider": meta.get("resolved_provider"),
                   "resolved_model": meta.get("resolved_model"),
                   "max_tokens": a.max_tokens,
                   "temperature": a.temp, "frequency_penalty": a.fp,
                   "presence_penalty": a.pp, "rows": rows},
                  open(a.out, "w"), ensure_ascii=False, indent=1)

    errors = [r for r in rows if r.get("kind") == "error"]
    if errors:
        out_failed = a.out.replace(".json", ".failed.json")
        json.dump({"dir": a.dir, "model": a.model, "max_tokens": a.max_tokens,
                   "aborted": True, "errors": len(errors), "rows": rows},
                  open(out_failed, "w"), ensure_ascii=False, indent=1)
        if os.path.exists(a.out):
            os.remove(a.out)
        print("\nabort_transport: %d/%d requests failed (%s) -> %s; result discarded"
              % (len(errors), len(rows), errors[0].get("error"), out_failed))
        sys.exit(2)

    ok_n = sum(1 for r in rows if r["ok"])
    loops = sum(1 for r in rows if r["kind"] == "loop")
    print("\nTOTAL: %d/%d correct (%.0f%% errors) | loops: %d"
          % (ok_n, len(rows), 100.0 * (len(rows) - ok_n) / max(len(rows), 1), loops))
    print("file:", a.out)


if __name__ == "__main__":
    main()
