#!/usr/bin/env python3
"""Build per-task matrices from result files.

Rows: one run (model + language + budget + variant). Columns: one task.
Cell: "<seconds>s <mark>". Marks: ✓ correct, ✗ wrong, L stopped on the length
cap, R aborted by the loop guard, · task not in this set.

Writes docs/results-by-task.md and prints the block for the README.
"""
import glob
import json
import os
import re

OK, BAD, LEN, LOOP, NA = "✓", "✗", "L", "R", "·"


def classify(path):
    """Return (kind, lang, budget, subset, variant) from a result filename."""
    name = os.path.basename(path)
    if name == "series.json":
        return None
    m = re.match(r"chains_(\w\w)_20k_(\d+)k?(.*)\.json$", name)
    if m:
        tail = m.group(3).strip("_")
        return "chains", m.group(1), m.group(2), ("8tasks" in tail), tail or "default"
    if name.startswith("programs_"):
        nums = re.findall(r"(\d+)", name)
        budget = nums[1] if len(nums) > 1 else (nums[0] if nums else "?")
        variant = "guarded" if "guarded" in name else ("legacy" if re.search(r"v[12]_", name) else "default")
        return "programs", "-", budget, False, variant
    return None


def load(path):
    d = json.load(open(path))
    rows = d if isinstance(d, list) else (d.get("rows") or [])
    out = {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        tid = r.get("id") if "id" in r else r.get("file")
        if tid is None:
            continue
        mark = OK if r.get("ok") else (LOOP if r.get("kind") == "loop"
                                      else (LEN if r.get("finish") == "length" else BAD))
        lat = r.get("latency_s")
        out[str(tid)] = (mark, round(lat) if isinstance(lat, (int, float)) else None)
    meta = {} if isinstance(d, list) else d
    return out, meta


def collect():
    chains, programs = [], []
    for path in sorted(glob.glob("results/*/*.json")):
        folder = path.split("/")[1]
        if folder.startswith("_"):
            continue
        info = classify(path)
        if info is None:
            continue
        kind, lang, budget, subset, variant = info
        tasks, meta = load(path)
        if not tasks:
            continue
        row = {"model": meta.get("resolved_model") or folder, "folder": folder,
               "lang": lang, "budget": budget, "subset": subset,
               "variant": variant, "tasks": tasks, "file": os.path.basename(path)}
        (chains if kind == "chains" else programs).append(row)
    return chains, programs


def sort_key(x):
    m = re.search(r"(\d+)", x)
    return (int(m.group(1)) if m else 10 ** 6, str(x))


def ids_for(rows):
    ids = []
    for r in rows:
        for t in r["tasks"]:
            if t not in ids:
                ids.append(t)
    return sorted(ids, key=sort_key)


def col_label(kind, task):
    if kind == "programs":
        m = re.search(r"seed(\d+)", task)
        return "S" + m.group(1) if m else str(task)
    return "T" + str(task)


def cell(t):
    if not t:
        return NA
    mark, lat = t
    return "%s %s" % (("%ds" % lat) if lat is not None else "—", mark)


def table(rows, ids, kind):
    head = "| Run | " + " | ".join(col_label(kind, i) for i in ids) + " | Score |"
    sep = "|---|" + "---|" * len(ids) + "---|"
    lines = [head, sep]
    for r in rows:
        bk = "k" if str(r["budget"]).isdigit() and int(r["budget"]) <= 200 else ""
        label = "%s · %s · %s%s · %s" % (r["folder"], r["lang"], r["budget"], bk, r["variant"])
        cells = [cell(r["tasks"].get(i)) for i in ids]
        ok = sum(1 for i in ids if r["tasks"].get(i, ("",))[0] == OK)
        lines.append("| %s | %s | %d/%d |" % (label, " | ".join(cells), ok, len(ids)))
    return "\n".join(lines)


def main():
    chains, programs = collect()
    c17 = [r for r in chains if not r["subset"]]
    c8 = [r for r in chains if r["subset"]]

    parts = ["### Test 1 — full 17-task set\n",
             table(c17, ids_for(c17), "chains") if c17 else "_No runs yet._",
             "\n### Test 1 — 8-task subset\n",
             table(c8, ids_for(c8), "chains") if c8 else "_No runs yet._",
             "\n### Test 2 — 20 frozen programs\n",
             table(programs, ids_for(programs), "programs") if programs else "_No runs yet._"]
    block = "\n".join(parts)

    header = ("# Per-task results\n\n"
              "Generated from the result files by `scripts/build_task_tables.py`.\n"
              "Cell format: `seconds mark` — ✓ correct, ✗ wrong, L stopped on the length\n"
              "cap, R aborted by the loop guard, · task not in this set.\n\n")
    with open("docs/results-by-task.md", "w") as f:
        f.write(header + block + "\n")
    print(block)


if __name__ == "__main__":
    main()
