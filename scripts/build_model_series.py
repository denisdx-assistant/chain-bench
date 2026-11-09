#!/usr/bin/env python3
"""Rebuild results/<model>/series.json from the files that are actually on disk.

The per-model index drifted: it was written once when a series started and never updated
when later runs (larger budgets, replicates, sampler variants) landed next to it. This
regenerates it from the data, keeps any extra keys already recorded per file, and reports
what changed.
"""
import glob
import json
import os
import re
import statistics


def rows_of(path):
    data = json.load(open(path))
    return data if isinstance(data, list) else (data.get("rows") or [])


def describe(folder, name):
    kind = "programs" if name.startswith("programs_") else "chains"
    lang = "-"
    m = re.search(r"_(ru|en|zh)_", name)
    if m:
        lang = m.group(1)
    nums = re.findall(r"(\d+)k", name)
    budget = (nums[-1] + "k") if nums else "?"
    note = "programs" if kind == "programs" else ("subset 8" if "8tasks" in name else "full 17")
    if name.endswith("_t03.json"):
        note += " · t 0.3 pen 0.2"
    if "rep2" in name:
        note += " · replicate"
    return kind, lang, budget, note


def main():
    for folder in sorted(glob.glob("results/*/")):
        model = os.path.basename(folder.rstrip("/"))
        if model.startswith("_") or model == "context":
            continue
        files = [p for p in sorted(glob.glob(folder + "*.json")) if not p.endswith("series.json")]
        if not files:
            continue
        path = os.path.join(folder, "series.json")
        prev = {}
        meta = {}
        if os.path.exists(path):
            try:
                old = json.load(open(path))
                meta = {k: v for k, v in old.items() if k != "series"}
                prev = {e.get("file"): e for e in old.get("series", [])}
            except Exception:
                pass
        series = []
        for p in files:
            name = os.path.basename(p)
            try:
                rows = rows_of(p)
            except Exception:
                continue
            if not rows:
                continue
            ok = sum(1 for r in rows if r.get("ok"))
            lat = [r.get("latency_s") or 0 for r in rows]
            gen = [(r.get("server_timings") or {}).get("predicted_per_second")
                   for r in rows if (r.get("server_timings") or {}).get("predicted_per_second")]
            tok = [(r.get("server_timings") or {}).get("predicted_n") or 0 for r in rows]
            kind, lang, budget, note = describe(folder, name)
            entry = {
                "file": name, "test": "test2_programs" if kind == "programs" else "test1_chains",
                "language": lang, "budget": budget, "note": note,
                "tasks": len(rows), "correct": ok,
                "error_pct": round(100 * (len(rows) - ok) / len(rows), 1),
                "median_latency_s": round(statistics.median(lat)) if lat else None,
                "median_gen_tps": round(statistics.median(gen), 1) if gen else None,
                "median_answer_tokens": round(statistics.median(tok)) if tok else None,
                "loops": sum(1 for r in rows if r.get("kind") == "loop"),
                "length_cut": sum(1 for r in rows if r.get("finish") == "length"),
                "unresolved": sum(1 for r in rows
                                  if r.get("kind") == "no_answer"
                                  or (not r.get("ok") and r.get("got") is None
                                      and r.get("finish") != "length"
                                      and r.get("kind") not in ("loop", "timeout", "error"))),
            }
            for k, v in (prev.get(name) or {}).items():
                entry.setdefault(k, v)
            series.append(entry)
        meta.setdefault("model", model)
        meta["series"] = series
        old_text = json.dumps(prev, sort_keys=True) if prev else ""
        new_text = json.dumps({e["file"]: e for e in series}, sort_keys=True)
        if old_text != new_text:
            json.dump(meta, open(path, "w"), ensure_ascii=False, indent=1)
            print("%-46s %d записей (было %d)" % (model, len(series), len(prev)))


if __name__ == "__main__":
    main()
