#!/usr/bin/env python3
"""Build results/<model>/series.json from the run files in that folder.

Deterministic: everything is recomputed from the result JSONs, so the index can
always be rebuilt after a resume. Run order follows the series order used by
scripts/run_series_q8.sh (full chains -> 8-task subsets -> programs).

Usage: python3 scripts/build_series_index.py results/Qwen3.8-27B-UD-Q8_K_XL
"""
import glob
import json
import os
import re
import statistics
import sys

LANGS = ("ru", "en", "zh")
ORDER = (["chains_%s_20k_16k.json" % l for l in LANGS]
         + ["chains_%s_20k_16k_8tasks.json" % l for l in LANGS]
         + ["programs_v4_16k.json"])


def kind_of(name):
    if name.startswith("chains_"):
        return "test1_chains"
    if name.startswith("programs_"):
        return "test2_programs"
    return None


def lang_of(name):
    m = re.match(r"chains_(\w\w)_", name)
    return m.group(1) if m else "-"


def budget_of(name):
    m = re.findall(r"_(\d+)k", name)
    return int(m[-1]) * 1000 if m else 16000


def kind_of_programs(name):
    return "test2_programs_v2" if re.search(r"programs_v[12]_", name) else "test2_programs"


def note_of(name, tasks):
    if "_8tasks" in name:
        return "8-task trilingual subset"
    if name.startswith("programs_") and re.search(r"programs_v[12]_", name):
        return ("legacy 8-program hard set" if "hard" in name
                else "legacy 8-program flow set")
    if name.startswith("programs_"):
        return "20 frozen programs v4"
    return ("full 17-task set, default sampling" if tasks == 17
            else "8-task trilingual subset (legacy filename)")


def entry(path):
    name = os.path.basename(path)
    d = json.load(open(path))
    rows = d if isinstance(d, list) else (d.get("rows") or [])
    n = len(rows)
    ok = sum(1 for r in rows if r.get("ok"))
    lat = [r["latency_s"] for r in rows if isinstance(r.get("latency_s"), (int, float))]
    rch = [r["reasoning_chars"] for r in rows
           if isinstance(r.get("reasoning_chars"), (int, float))]
    meta = {} if isinstance(d, list) else d
    return {
        "file": name,
        "tasks": n,
        "correct": ok,
        "error_pct": round(100.0 * (n - ok) / n) if n else 0,
        "median_latency_s": round(statistics.median(lat)) if lat else None,
        "loops": sum(1 for r in rows if r.get("kind") == "loop"),
        "length_cut": sum(1 for r in rows if r.get("finish") == "length"),
        "median_reasoning_chars": round(statistics.median(rch)) if rch else None,
        "max_tokens": meta.get("max_tokens"),
        "test": (kind_of_programs(name) if name.startswith("programs_")
                 else kind_of(name)),
        "language": lang_of(name),
        "budget": budget_of(name),
        "note": note_of(name, n),
    }


def main(folder):
    names = {os.path.basename(p) for p in glob.glob(os.path.join(folder, "*.json"))}
    names.discard("series.json")
    names = {n for n in names if kind_of(n)}
    ordered = [n for n in ORDER if n in names]
    ordered += sorted(names - set(ordered))
    series = [entry(os.path.join(folder, n)) for n in ordered]

    model = os.path.basename(folder.rstrip("/"))
    langs = sorted({s["language"] for s in series if s["language"] != "-"})
    frozen = {"chains": [],
              "programs": "v4/20" if "programs_v4_16k.json" in names else None}
    for lang in ("ru", "en", "zh"):
        if "chains_%s_20k_16k.json" % lang in names:
            frozen["chains"].append("%s/17" % lang)
        if "chains_%s_20k_16k_8tasks.json" % lang in names:
            frozen["chains"].append("%s/8" % lang)

    out = {
        "model": model,
        "notes": "27B, UD Q8_K_XL quantisation. Context 150k, budget 16k, "
                 "guarded runner (streaming loop guard).",
        "series": series,
        "frozen_datasets": frozen,
    }
    dest = os.path.join(folder, "series.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote %s (%d runs, langs %s)" % (dest, len(series), ",".join(langs) or "-"))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
