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
import sys
import re

OK, BAD, LEN, LOOP, NA = "✓", "✗", "L", "R", "·"

RUN_CONFIGS = {}
if os.path.exists("results/run-configs.json"):
    RUN_CONFIGS = {k: v for k, v in json.load(open("results/run-configs.json")).items()
                   if not k.startswith("_")}


def cfg_for(folder, file):
    return RUN_CONFIGS.get("%s/%s" % (folder, file), {})


def cfg_label(cfg, budget):
    if not cfg:
        return "budget %s" % budget
    parts = ["ctx %s" % cfg.get("ctx", "?"),
             "YaRN" if cfg.get("yarn") else "no YaRN",
             "T %s" % cfg.get("temp", "default")]
    pen = cfg.get("penalty", "-")
    if pen and pen != "-":
        parts.append("pen %s" % pen)
    # budget is a cap, not a comparison parameter: recorded in results/run-configs.json

    if cfg.get("guard"):
        parts.append("guard")
    if cfg.get("note"):
        parts.append(cfg["note"])
    if cfg.get("reasoning") not in (None, "default"):
        parts.append("reasoning %s" % cfg["reasoning"])
    if cfg.get("provenance") == "inferred":
        parts.append("provenance inferred")
    return " · ".join(parts)


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
        if "id" in r:
            tid = r["id"]
        elif "file" in r and r["file"]:
            m = re.search(r"seed(\d+)", str(r["file"]))
            tid = "S" + m.group(1) if m else str(r["file"])
        elif "seed" in r:
            tid = "S" + str(r["seed"])
        else:
            continue
        mark = OK if r.get("ok") else (LOOP if r.get("kind") == "loop"
                                      else (LEN if r.get("finish") == "length" else BAD))
        lat = r.get("latency_s")
        gen = None
        st = r.get("server_timings") or {}
        if isinstance(st, dict) and isinstance(st.get("predicted_ms"), (int, float)):
            # compute time for this task: prefill + generation, both reported by the server
            gen = round(((st.get("prompt_ms") or 0) + st["predicted_ms"]) / 1000.0)
        out[str(tid)] = (mark, round(lat) if isinstance(lat, (int, float)) else None, gen)
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
               "variant": variant, "tasks": tasks, "file": os.path.basename(path),
               "expected": expected_items(kind, subset, os.path.basename(path)),
               "partial": len(tasks) < expected_items(kind, subset, os.path.basename(path))}
        (chains if kind == "chains" else programs).append(row)
    return chains, programs


def expected_items(kind, subset, name=""):
    if kind == "programs":
        # the frozen v4 set has 20 programs; the legacy v2 sets have 8
        return 8 if re.search(r"v2_|_8\.json", name) else 20
    return 8 if subset else 17


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
        m = re.search(r"seed(\d+)", str(task)) or re.match(r"S(\d+)$", str(task))
        return "S" + m.group(1) if m else str(task)
    return "T" + str(task)


def cell(t):
    if not t:
        return NA
    mark, lat, gen = (t + (None,))[:3] if len(t) == 2 else t
    secs = gen if gen is not None else lat
    suffix = "" if gen is not None else ("w" if lat is not None else "")
    return "%s%s %s" % (("%ds" % secs) if secs is not None else "—", suffix, mark)


def table(rows, ids, kind):
    head = "| Run | " + " | ".join(col_label(kind, i) for i in ids) + " | Score |"
    sep = "|---|" + "---|" * len(ids) + "---|"
    lines = [head, sep]
    for r in rows:
        bk = "k" if str(r["budget"]).isdigit() and int(r["budget"]) <= 200 else ""
        label = "%s · %s · %s%s · %s" % (r["folder"], r["lang"], r["budget"], bk, r["variant"])
        cells = [cell(r["tasks"].get(i)) for i in ids]
        ok = sum(1 for i in ids if r["tasks"].get(i, ("",))[0] == OK)
        if r.get("partial"):
            done = len(r["tasks"])
            lines.append("| %s | %s | %d/%d (partial %d/%d) |"
                         % (label, " | ".join(cells), ok, done, done, r.get("expected", done)))
        else:
            lines.append("| %s | %s | %d/%d |" % (label, " | ".join(cells), ok, len(ids)))
    return "\n".join(lines)



def human(seconds):
    """12m34s / 95s"""
    if seconds is None:
        return "—"
    seconds = int(round(seconds))
    if seconds < 60:
        return "%ds" % seconds
    return "%dm%02ds" % (seconds // 60, seconds % 60)


def summary():
    """Compact cross-test matrix: rows are runs, columns are test groups."""
    chains, programs = collect()
    groups = {}
    for r in chains + programs:
        cfg = cfg_for(r["folder"], r["file"])
        sig = (r["folder"], cfg.get("ctx"), cfg.get("yarn"), cfg.get("temp"),
               cfg.get("penalty"), bool(cfg.get("guard")))
        groups.setdefault(sig, {"chains": [], "programs": [], "cfg": cfg})
        groups[sig]["programs" if r["file"].startswith("programs_") else "chains"].append(r)

    rows = []
    for (folder, _ctx, _yarn, _temp, _pen, _guard), g in sorted(groups.items(), key=lambda kv: str(kv[0])):
        def pick(lang):
            full = [r for r in g["chains"] if r["lang"] == lang and not r["subset"] and not r.get("partial")]
            if full:
                full.sort(key=lambda r: (r["variant"] != "guarded", -len(r["tasks"])))
                return full[0], False
            sub = [r for r in g["chains"] if r["lang"] == lang and not r.get("partial")]
            if sub:
                sub.sort(key=lambda r: -len(r["tasks"]))
                return sub[0], True
            return None, False

        cells = {}
        total_t = total_ok = total_n = 0
        for lang in ("en", "ru", "zh"):
            r, subset = pick(lang)
            if r is None:
                cells["t1_" + lang] = None
                continue
            t = sum(((v[2] if len(v) > 2 and v[2] is not None else v[1]) or 0)
                    for v in r["tasks"].values())
            ok = sum(1 for v in r["tasks"].values() if v[0] == OK)
            n = len(r["tasks"])
            cells["t1_" + lang] = {"t": t, "ok": ok, "n": n, "subset": subset}
            total_t += t; total_ok += ok; total_n += n

        complete_programs = [r for r in g["programs"] if not r.get("partial")]
        pr = complete_programs[0] if complete_programs else None
        if pr:
            t = sum(((v[2] if len(v) > 2 and v[2] is not None else v[1]) or 0)
                    for v in pr["tasks"].values())
            ok = sum(1 for v in pr["tasks"].values() if v[0] == OK)
            n = len(pr["tasks"])
            cells["t2"] = {"t": t, "ok": ok, "n": n}
            total_t += t; total_ok += ok; total_n += n
        else:
            cells["t2"] = None

        budget = g["cfg"].get("budget", g["chains"][0]["budget"] if g["chains"] else g["programs"][0]["budget"])
        rows.append({"label": "%s · %s" % (folder, cfg_label(g["cfg"], budget)),
                     "cells": cells, "overall": (total_t, total_ok, total_n)})

    head = "| Run | Overall (errors) | Test 1 en (correct) | Test 1 ru (correct) | Test 1 zh (correct) | Test 2 (correct) |"
    sep = "|---|---|---|---|---|---|"
    lines = [head, sep]
    for r in rows:
        def fmt(c):
            if not c:
                return "—"
            mark = "%d/%d" % (c["ok"], c["n"])
            if c.get("subset"):
                mark += " (8)"
            return "%s %s" % (human(c["t"]), mark)
        t, ok, n = r["overall"]
        overall = ("%s · %d%% err" % (human(t), round(100 * (n - ok) / n))) if n else "—"
        lines.append("| %s | %s | %s | %s | %s | %s |" % (
            r["label"], overall, fmt(r["cells"]["t1_en"]), fmt(r["cells"]["t1_ru"]),
            fmt(r["cells"]["t1_zh"]), fmt(r["cells"]["t2"])))
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
    if "--summary" in sys.argv:
        print(summary())
    else:
        main()
