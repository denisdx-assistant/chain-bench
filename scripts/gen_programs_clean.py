#!/usr/bin/env python3
"""Generate the clean program set: same operations, no decoys at all.

Seeds match the noisy v4 set (300-319), ops=20, comments/extras/traps=0.
Expected values are obtained by executing each program, never computed by hand.

  python3 scripts/gen_programs_clean.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_program_v3 as g

OUT = os.path.join("datasets", "programs", "v4_clean")
SEEDS = range(300, 320)
OPS = 20


def main():
    os.makedirs(OUT, exist_ok=True)
    made = 0
    for seed in SEEDS:
        code, _ = g.gen(seed, OPS, 0, 0, 0)
        ns = {}
        exec(compile(code, "seed%d" % seed, "exec"), ns)
        arr = ns.get("arr")
        if not isinstance(arr, list) or len(arr) != 10:
            raise SystemExit("seed %d produced no valid array" % seed)
        base = os.path.join(OUT, "v4c_seed%d" % seed)
        with open(base + ".py", "w") as f:
            f.write(code)
        json.dump({"seed": seed,
                   "params": {"comments": 0, "extras": 0, "traps": 0, "ops": OPS},
                   "lines": code.count("\n"),
                   "expected_array": json.dumps(arr),
                   "expected_sum": sum(arr)},
                  open(base + ".json", "w"), ensure_ascii=False, indent=1)
        made += 1
    print("clean programs written: %d to %s" % (made, OUT))


if __name__ == "__main__":
    main()
