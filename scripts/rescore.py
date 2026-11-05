#!/usr/bin/env python3
"""Re-score stored answers without touching the model.

Reads result files, re-parses the raw answer with the tolerant parser and
recomputes the score. Prints a diff against the stored score; `--write` saves
the recomputed verdict alongside the original one (never overwrites it).

Why: a strict parser can mark a correct answer wrong when the model formats it
differently. Keeping the raw text makes that check possible later.

Usage:
  python3 scripts/rescore.py                     # audit every result file
  python3 scripts/rescore.py --write             # also store rescore results
  python3 scripts/rescore.py results/<model>/programs_v4_16k.json
"""
import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_frozen_guarded import parse_array, parse_sum


def as_list(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        try:
            return json.loads(x.replace("'", '"'))
        except Exception:
            nums = [int(v) for v in re.findall(r"-?\d+", x)]
            return nums or None
    return None


def rescore_programs(rows):
    changed = []
    for r in rows:
        raw = r.get("raw")
        # legacy sets stored only the parsed number, not the model's answer
        if "got_array" not in r and "got" in r:
            ok = r.get("got") == r.get("expected")
            r["ok_rescored"] = ok
            if ok != bool(r.get("ok")):
                changed.append({"item": r.get("seed"), "stored": bool(r.get("ok")),
                                "rescored": ok, "note": "legacy numeric format"})
            continue
        if not raw:
            continue
        exp_a = as_list(r.get("expected_array"))
        exp_s = r.get("expected_sum", r.get("expected"))
        got_a, got_s = parse_array(raw), parse_sum(raw)
        ok = exp_a is not None and got_a == exp_a and got_s == exp_s
        if ok != bool(r.get("ok")):
            changed.append({"item": r.get("file") or r.get("seed"),
                            "stored": bool(r.get("ok")), "rescored": ok,
                            "parsed_array": got_a, "parsed_sum": got_s})
        r["ok_rescored"] = ok
        r["parsed_array_rescored"] = got_a
        r["parsed_sum_rescored"] = got_s
    return changed


def rescore_chains(rows):
    changed = []
    for r in rows:
        raw = r.get("raw")
        if raw is None:
            continue
        m = re.findall(r"-?\d+", str(raw).replace("−", "-"))
        got = int(m[-1]) if m else None
        ok = got == r.get("answer")
        if ok != bool(r.get("ok")):
            changed.append({"item": r.get("id"), "stored": bool(r.get("ok")),
                            "rescored": ok, "parsed": got})
        r["ok_rescored"] = ok
        r["parsed_rescored"] = got
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    paths = a.paths or sorted(glob.glob("results/*/*.json"))
    for p in paths:
        if os.path.basename(p) == "series.json":
            continue
        d = json.load(open(p))
        rows = d if isinstance(d, list) else (d.get("rows") or [])
        if not rows:
            continue
        is_programs = any("file" in r or "seed" in r for r in rows[:3])
        changed = rescore_programs(rows) if is_programs else rescore_chains(rows)
        stored = sum(1 for r in rows if r.get("ok"))
        rescored = sum(1 for r in rows if r.get("ok_rescored"))
        with_raw = sum(1 for r in rows if r.get("raw") is not None)
        print("%-58s rows %2d | raw %2d | stored %2d | rescored %2d | changed %d"
              % (p.replace("results/", ""), len(rows), with_raw, stored, rescored, len(changed)))
        for c in changed[:5]:
            print("    ", c)
        if a.write and not isinstance(d, list):
            d["rescored_at"] = "manual"
            json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
