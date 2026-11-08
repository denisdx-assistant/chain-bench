#!/usr/bin/env python3
"""Check whether prefill and generation overlapped inside a run.

Some providers serve with continuous batching: a new request's prefill is chunked in
between decode steps of other requests. When that happens the server's own
`prompt_ms` and `predicted_ms` no longer add up to the wall time — the sum exceeds it,
because both were happening at once — and neither number describes a clean measurement.

A row is additive when, within noise, prompt_ms + predicted_ms <= wall. Everything else
is reported so the affected rows can be excluded from speed tables.

Usage: python3 scripts/check_overlap.py [--write]
"""
import glob
import json
import os
import sys


def rows_of(path):
    try:
        data = json.load(open(path))
    except Exception:
        return []
    return data if isinstance(data, list) else (data.get("rows") or [])


def scan():
    out = []
    for path in sorted(glob.glob("results/*/*.json")):
        if any(x in path for x in ("_retries", "_archive", "_raw")):
            continue
        rows, overlaps, ratios = rows_of(path), 0, []
        for r in rows:
            st = r.get("server_timings") or {}
            prompt_ms, gen_ms = st.get("prompt_ms"), st.get("predicted_ms")
            wall = r.get("wall_s") or r.get("latency_s") or r.get("seconds")
            if not (prompt_ms and gen_ms and wall):
                continue
            total = prompt_ms + gen_ms
            if total and wall * 1000 < total * 0.95:
                overlaps += 1
            if total:
                ratios.append(wall * 1000 / total)
        if ratios:
            ratios.sort()
            out.append({"file": path, "rows": len(rows), "overlaps": overlaps,
                        "wall_over_sum": round(ratios[len(ratios) // 2], 3)})
    return out


def main():
    data = scan()
    bad = [d for d in data if d["overlaps"]]
    print("%-60s %6s %8s %10s" % ("file", "rows", "overlaps", "wall/sum"))
    for d in data:
        print("%-60s %6d %8d %10.2f" % (d["file"][:60], d["rows"], d["overlaps"], d["wall_over_sum"]))
    print()
    if bad:
        print("%d file(s) contain rows where prefill and generation overlapped:" % len(bad))
        for d in bad:
            print("  %s: %d of %d rows" % (d["file"], d["overlaps"], d["rows"]))
    else:
        print("No overlap: prompt_ms + predicted_ms match the wall time everywhere, "
              "so these runs were single-client and sequential.")
    if "--write" in sys.argv:
        json.dump(data, open("results/_overlap.json", "w"), ensure_ascii=False, indent=1)
        print("written to results/_overlap.json")


if __name__ == "__main__":
    main()
