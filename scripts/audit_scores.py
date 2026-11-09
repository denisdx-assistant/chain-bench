#!/usr/bin/env python3
"""Audit how every recorded row was scored: answered-wrong versus not-answered.

A reply that carries no parseable number (chains) or no ARRAY/SUM (programs) is not
evidence that the model cannot solve the task — at a small budget it may have spent
everything on reasoning. Such rows must be retried at a larger budget instead of being
counted as failures. A row is only a real failure once a retry at a bigger budget also
fails.

Categories: ok | wrong | no_answer | length_cut | loop | transport.

Retry resolution: any task id that appears in a folder's `_retries` folder is treated as
resolved, because the retry is the authoritative second attempt for that task.

Usage: python3 scripts/audit_scores.py [--json out.json]
"""
import glob
import json
import os
import re
import sys


def rows_of(path):
    try:
        data = json.load(open(path))
    except Exception:
        return []
    return data if isinstance(data, list) else (data.get("rows") or [])


def _program_parsed(row):
    if "got_array" in row or "got_sum" in row:
        return row.get("got_array") is not None or row.get("got_sum") is not None
    text = row.get("raw") or ""
    has_arr = any(len(re.findall(r"-?\d+", b)) == 10
                  for b in re.findall(r"\[([^\[\]]{0,200})\]", text))
    has_sum = bool(re.search(r"\b(sum|total)\b[^0-9\-]{0,20}-?\d+", text, re.I))
    return has_arr or has_sum


def classify(row):
    if row.get("ok"):
        return "ok"
    if row.get("kind") == "error" or row.get("error"):
        return "transport"
    if row.get("finish") == "length":
        return "length_cut"
    if row.get("kind") == "loop":
        return "loop"
    if row.get("kind") == "timeout":
        return "no_answer"
    if "arr_ok" in row or "sum_ok" in row or "got_array" in row:
        return "wrong" if _program_parsed(row) else "no_answer"
    return "wrong" if row.get("got") is not None else "no_answer"


def retried_ids(folder):
    ids = set()
    for path in glob.glob(os.path.join(folder, "_retries", "*.json")):
        for r in rows_of(path):
            key = r.get("id")
            if key is None and r.get("file"):
                key = str(r["file"]).split("/")[-1]
            if key is not None:
                ids.add(str(key))
    return ids


def main():
    report, total_unresolved = [], 0
    for path in sorted(glob.glob("results/*/*.json")):
        folder = os.path.dirname(path)
        if os.path.basename(folder).startswith("_"):
            continue
        rows = rows_of(path)
        if not rows:
            continue
        retried = retried_ids(folder)
        pending = []
        for r in rows:
            kind = classify(r)
            if kind in ("ok", "wrong"):
                continue
            key = r.get("id")
            if key is None and r.get("file"):
                key = str(r["file"]).split("/")[-1]
            if key is not None and str(key) in retried:
                continue  # already answered by the retry at a bigger budget
            pending.append({"id": key, "kind": kind})
        if pending:
            total_unresolved += len(pending)
            report.append({"file": path, "rows": len(rows), "pending": pending})

    for r in report:
        names = ", ".join("%s=%s" % (p["id"], p["kind"]) for p in r["pending"])
        print("%-58s %s" % (r["file"][:58], names))
    print("\n%d unresolved row(s) in %d file(s): these were scored as failures but never got "
          "an answer, so they need a retry at a larger budget" % (total_unresolved, len(report)))
    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        json.dump(report, open(out, "w"), ensure_ascii=False, indent=1)
        print("written to", out)


if __name__ == "__main__":
    main()
