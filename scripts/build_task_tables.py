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
import statistics

OK, BAD, LEN, LOOP, NA = "✓", "✗", "L", "R", "·"
UNANS = "?"  # no answer at all: not scored either way

RUN_CONFIGS = {}
if os.path.exists("results/run-configs.json"):
    RUN_CONFIGS = {k: v for k, v in json.load(open("results/run-configs.json")).items()
                   if not k.startswith("_")}


def cfg_for(folder, file):
    return RUN_CONFIGS.get("%s/%s" % (folder, file), {})


def cfg_label(cfg, budget):
    """Only what differs from the plain model: context and YaRN are details, not labels.

    A run on the model's own defaults carries no label at all; a run with a changed sampler
    says which sampler, nothing else. Everything else lives in results/run-configs.json and
    the detailed pages.
    """
    if not cfg:
        return ""
    parts = []
    temp = cfg.get("temp")
    if temp not in (None, "", "default"):
        parts.append("t %s" % temp)
    pen = cfg.get("penalty")
    if pen and pen != "-" and re.fullmatch(r"[0-9.\s/]+", str(pen)):
        parts.append("pen %s" % pen)
    if cfg.get("reasoning") not in (None, "default"):
        parts.append("reasoning %s" % cfg["reasoning"])
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
        # a reply with no parseable answer is unresolved, not a failure: "?" keeps it out of
        # both the numerator and the denominator until a retry at a bigger budget decides
        mark = OK if r.get("ok") else (LOOP if r.get("kind") == "loop"
                                      else (LEN if r.get("finish") == "length"
                                            else (UNANS if (r.get("kind") == "no_answer"
                                                           or unanswered(r)) else BAD)))
        lat = r.get("latency_s")
        gen = None
        st = r.get("server_timings") or {}
        if isinstance(st, dict) and isinstance(st.get("predicted_ms"), (int, float)):
            # compute time for this task: prefill + generation, both reported by the server
            gen = round(((st.get("prompt_ms") or 0) + st["predicted_ms"]) / 1000.0)
        tok = st.get("predicted_n") if isinstance(st, dict) else None
        out[str(tid)] = (mark, round(lat) if isinstance(lat, (int, float)) else None, gen, tok)
    meta = {} if isinstance(d, list) else d
    return out, meta


def unanswered(r):
    """True when the reply carried no answer at all, which is not the same as a wrong one.

    Older files stored such rows as plain failures, so the mark is derived from the data
    rather than from the recorded kind: a chain row without a parsed integer, or a program
    row with neither a ten-number array nor a SUM, never answered.
    """
    if r.get("ok") or r.get("finish") == "length" or r.get("kind") in ("loop", "timeout", "error"):
        return False
    if "got_array" in r or "got_sum" in r:
        if r.get("got_array") is not None or r.get("got_sum") is not None:
            return False
    if "arr_ok" in r or "sum_ok" in r:
        text = r.get("raw") or ""
        has_arr = any(len(re.findall(r"-?\d+", b)) == 10
                      for b in re.findall(r"\[([^\[\]]{0,200})\]", text))
        has_sum = bool(re.search(r"\b(sum|total)\b[^0-9\-]{0,20}-?\d+", text, re.I))
        return not (has_arr or has_sum)
    return r.get("got") is None



def retry_verdicts(folder):
    """Verdicts from a folder's `_retries` files: the authoritative second attempt.

    A row that was cut by the budget or produced no answer is unresolved in the main file.
    If a retry exists and it did produce an answer, that verdict is the one to use.
    """
    verdicts = {}
    for path in glob.glob(os.path.join(folder, "_retries", "*.json")):
        try:
            data = json.load(open(path))
        except Exception:
            continue
        rows = data if isinstance(data, list) else (data.get("rows") or [])
        for r in rows:
            if not isinstance(r, dict):
                continue
            key = r.get("id")
            if key is None and r.get("file"):
                key = str(r["file"]).split("/")[-1]
            if key is None or r.get("finish") == "length":
                continue
            if r.get("ok"):
                verdicts[str(key)] = OK
            elif r.get("got") is not None or r.get("ok") is False:
                # a parsed answer, or an explicit miss, is a real verdict
                if r.get("got") is not None:
                    verdicts[str(key)] = BAD
    return verdicts



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
        # an unresolved row with a retry gets the retry's verdict
        fixes = retry_verdicts("results/" + folder)
        for key, mark in list(tasks.items()):
            if mark[0] in (LEN, UNANS) and str(key) in fixes:
                tasks[key] = (fixes[str(key)],) + tuple(mark[1:])
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
    t = tuple(t) + (None,) * (4 - len(t))
    mark, lat, gen = t[0], t[1], t[2]
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
        # the loop guard is on for every canonical run, so it is not part of the identity;
        # including it split otherwise identical samples into separate rows
        sig = (r["folder"], cfg.get("ctx"), cfg.get("yarn"), cfg.get("temp"),
               cfg.get("penalty"))
        groups.setdefault(sig, {"chains": [], "programs": [], "cfg": cfg})
        groups[sig]["programs" if r["file"].startswith("programs_") else "chains"].append(r)

    def cell_of(r):
        t = sum(((v[2] if len(v) > 2 and v[2] is not None else v[1]) or 0)
                for v in r["tasks"].values())
        ok = sum(1 for v in r["tasks"].values() if v[0] == OK)
        # unanswered rows stay out of the denominator: no answer is not a wrong answer
        # both a cut and a silent reply are unresolved: they need a retry, not a verdict
        n = sum(1 for v in r["tasks"].values() if v[0] in (OK, BAD, LOOP))
        return {"t": t, "ok": ok, "n": n}

    def avg_cells(cells):
        """Mean over repeated runs of the same configuration: a cell may be fractional."""
        cells = [c for c in cells if c]
        if not cells:
            return None
        if len(cells) == 1:
            out = dict(cells[0])
            out["runs"] = 1
            return out
        return {"t": sum(c["t"] for c in cells) / len(cells),
                "ok": sum(c["ok"] for c in cells) / len(cells),
                "n": sum(c["n"] for c in cells) / len(cells),
                "runs": len(cells)}

    rows = []
    for (folder, _ctx, _yarn, _temp, _pen), g in sorted(groups.items(), key=lambda kv: str(kv[0])):
        def pick(lang):
            """Every valid full run of the language; several runs average into one cell."""
            full = [r for r in g["chains"] if r["lang"] == lang and not r["subset"] and not r.get("partial")]
            if full:
                return full, False
            sub = [r for r in g["chains"] if r["lang"] == lang and not r.get("partial")]
            if sub:
                return sub, True
            return [], False

        cells = {}
        total_t = total_ok = total_n = 0
        for lang in ("en", "ru", "zh"):
            runs, subset = pick(lang)
            c = avg_cells([cell_of(r) for r in runs])
            if c is None:
                cells["t1_" + lang] = None
                continue
            c["subset"] = subset
            cells["t1_" + lang] = c
            total_t += c["t"]; total_ok += c["ok"]; total_n += c["n"]

        complete_programs = [r for r in g["programs"] if not r.get("partial")]
        _toks = []
        for _r in [c for c in g["chains"] if not c.get("partial")] + complete_programs:
            for _v in _r["tasks"].values():
                if len(_v) > 3 and isinstance(_v[3], int):
                    _toks.append(_v[3])
        # one subset run per language: prefer the one with server timings, else the first
        # subsets: one averaged cell per language, summed across the three languages
        _sub_parts = []
        _sub_langs = []
        for _lang in ("ru", "en", "zh"):
            _cand = [r for r in g["chains"] if r.get("subset") and r["lang"] == _lang and not r.get("partial")]
            if not _cand:
                continue
            _c = avg_cells([cell_of(r) for r in _cand])
            if _c:
                _sub_parts.append(_c)
                _sub_langs.append(_lang)
        if _sub_parts:
            cells["t1_subs"] = {"t": sum(c["t"] for c in _sub_parts),
                                "ok": sum(c["ok"] for c in _sub_parts),
                                "n": sum(c["n"] for c in _sub_parts),
                                "runs": max(c["runs"] for c in _sub_parts),
                                "langs": len(_sub_parts),
                                "lang_list": _sub_langs}
        else:
            cells["t1_subs"] = None
        c2 = avg_cells([cell_of(r) for r in complete_programs])
        if c2:
            cells["t2"] = c2
            total_t += c2["t"]; total_ok += c2["ok"]; total_n += c2["n"]
        else:
            # a set that was stopped early still reports what it actually ran
            partial_programs = [r for r in g["programs"] if r.get("partial")]
            if partial_programs:
                seen = {}
                for _r in partial_programs:
                    seen.update(_r["tasks"])
                ok_n = sum(1 for v in seen.values() if v[0] == OK)
                t_n = sum(((v[2] if len(v) > 2 and v[2] is not None else v[1]) or 0)
                          for v in seen.values())
                cells["t2"] = {"t": t_n, "ok": ok_n, "n": len(seen),
                               "partial_of": partial_programs[0]["expected"]}
            else:
                cells["t2"] = None

        budget = g["cfg"].get("budget", g["chains"][0]["budget"] if g["chains"] else g["programs"][0]["budget"])
        _tok = []
        for _r in g["chains"] + g["programs"]:
            if _r.get("partial"):
                continue
            for _v in _r["tasks"].values():
                pass
        # say out loud how many rows are unresolved, so a shorter denominator is explained
        unresolved = sum(1 for r in (g["chains"] + g["programs"])
                         for v in r["tasks"].values() if v[0] in (LEN, UNANS))
        extras = cfg_label(g["cfg"], budget)
        label = folder if not extras else "%s · %s" % (folder, extras)
        if unresolved:
            label += " · unresolved %d" % unresolved
        if not any(cells.get(k) for k in cells) and not complete_programs:
            continue
        rows.append({"label": label,
                     "median_tokens": round(statistics.median(_toks)) if _toks else None,
                     "cells": cells, "overall": (total_t, total_ok, total_n)})

    head = ("| Run | Overall (errors) | Median tokens/task | Test 1 en (correct) | Test 1 ru (correct) | "
            "Test 1 zh (correct) | Test 1 subsets 8 (all langs) | Test 2 (correct) |")
    sep = "|---|---|---|---|---|---|---|---|"
    lines = [head, sep]
    for r in rows:
        def mark(ok, n):
            if abs(ok - round(ok)) < 1e-9:
                return "%d/%d" % (round(ok), round(n))
            return "%.1f/%d" % (ok, round(n))

        def fmt(c):
            if not c:
                return "—"
            m = mark(c["ok"], c["n"])
            if c.get("langs", 3) < 3:
                m += " (%s only)" % "/".join(c.get("lang_list") or ["ru", "en", "zh"][:c["langs"]])
            elif c.get("subset"):
                m += " (8)"
            if c.get("partial_of"):
                m += " of %d run" % c["partial_of"]
            return "%s %s" % (human(c["t"]), m)
        t, ok, n = r["overall"]
        overall = ("%s · %d%% err" % (human(t), round(100 * (n - ok) / n))) if n else "—"
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["label"], overall,
            ("%d" % r["median_tokens"]) if r.get("median_tokens") else "—",
            fmt(r["cells"]["t1_en"]), fmt(r["cells"]["t1_ru"]),
            fmt(r["cells"]["t1_zh"]), fmt(r["cells"].get("t1_subs")), fmt(r["cells"]["t2"])))
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
