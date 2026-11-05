#!/usr/bin/env python3
"""Self-test for program scoring: guards against the wrong-key class of bug.

Run before trusting a series: python3 scripts/selftest_scoring.py
Exit code 0 means every case behaved as expected.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_frozen_guarded import score_program, expected_of, parse_array, parse_sum

EXP = {"expected_array": "[19, 19, 24, 63, 22, 44, 3, 20, 19, 97]", "expected_sum": 330}
GOOD = "ARRAY: [19, 19, 24, 63, 22, 44, 3, 20, 19, 97]\nSUM: 330"
ALT = "The final array is [19, 19, 24, 63, 22, 44, 3, 20, 19, 97] and the sum is 330."

CASES = [
    ("exact answer", EXP, GOOD, True),
    ("alternative wording", EXP, ALT, True),
    ("one element changed", EXP, GOOD.replace("24", "25"), False),
    ("sum changed", EXP, "ARRAY: [19, 19, 24, 63, 22, 44, 3, 20, 19, 97]\nSUM: 331", False),
    ("empty answer", EXP, "", False),
    ("truncated answer", EXP, "ARRAY: [19, 19, 24,", False),
    ("legacy schema", {"array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "sum": 55},
     "ARRAY: [1,2,3,4,5,6,7,8,9,10]\nSUM: 55", True),
]


def main():
    failures = 0
    for name, exp, answer, want in CASES:
        ok, ok_arr, ok_sum, _, _ = score_program(exp, answer)
        good = (ok == want)
        failures += 0 if good else 1
        print("%-22s ok=%-5s array=%-5s sum=%-5s %s"
              % (name, ok, ok_arr, ok_sum, "PASS" if good else "FAIL"))

    try:
        expected_of({"foo": "bar"})
        print("%-22s FAIL (no error raised)" % "missing schema")
        failures += 1
    except ValueError:
        print("%-22s PASS (schema error raised)" % "missing schema")

    print("\n%s" % ("ALL PASS" if failures == 0 else "%d FAILURE(S)" % failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
