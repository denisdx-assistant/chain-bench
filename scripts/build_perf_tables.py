#!/usr/bin/env python3
"""Per-run performance statistics from server-side timings.

For every result file it reports median generation speed, prefill speed, the
number of tokens spent on an answer and the size of the prompt (including the
cached part). Writes docs/performance.md; prints the same table.

Server fields come from llama.cpp-style `timings` in the response:
  prompt_n, prompt_ms, prompt_per_second, predicted_n, predicted_ms,
  predicted_per_second, cache_n
Runs made before these fields were captured show "—".
"""
import glob
import json
import os
import re
import statistics

OK, BAD, LEN, LOOP = "✓", "✗", "L", "R"


def classify(path):
    name = os.path.basename(path)
    m = re.match(r"chains_(\w\w)_20k_(\d+)k?(.*)\.json$", name)
    if m:
        tail = m.group(3).strip("_")
        return "chains", m.group(1), m.group(2), ("8tasks" in tail), tail or "default"
    if name.startswith("programs_"):
        nums = re.findall(r"(\d+)", name)
        budget = nums[1] if len(nums) > 1 else (nums[0] if nums else "?")
        return "programs", "-", budget, False, "guarded" if "guarded" in name else "default"
    return None


def median(values):
    vals = [v for v in values if isinstance(v, (int, float))]
    return statistics.median(vals) if vals else None


def main():
    rows_out = []
    for path in sorted(glob.glob("results/*/*.json")):
        folder = path.split("/")[1]
        if folder.startswith("_") or ".failed." in path or os.path.basename(path) == "series.json":
            continue
        info = classify(path)
        if info is None:
            continue
        kind, lang, budget, subset, variant = info
        d = json.load(open(path))
        rows = d if isinstance(d, list) else (d.get("rows") or [])
        if not rows:
            continue
        gen_tps, pre_tps, out_tok, prompt_tok, gen_s, uncached = [], [], [], [], [], []
        for r in rows:
            st = r.get("server_timings") or {}
            if not isinstance(st, dict):
                continue
            if st.get("predicted_per_second"):
                gen_tps.append(st["predicted_per_second"])
            if (st.get("cache_n") or 0) == 0 and st.get("prompt_per_second") and (st.get("prompt_n") or 0) >= 50:
                pre_tps.append(st["prompt_per_second"])
                uncached.append(1)
            if st.get("predicted_n"):
                out_tok.append(st["predicted_n"])
            pn = (st.get("prompt_n") or 0) + (st.get("cache_n") or 0)
            if pn:
                prompt_tok.append(pn)
            if st.get("predicted_ms"):
                gen_s.append(st["predicted_ms"] / 1000.0)
        ok = sum(1 for r in rows if r.get("ok"))
        stem = os.path.basename(path).replace(".json", "")
        label = "%s · %s · %s" % (folder, kind if kind == "programs" else "chains " + lang,
                                  budget + "k" if str(budget).isdigit() and int(budget) <= 200 else budget)
        if kind == "programs":
            label += " · " + stem.replace("programs_", "")
        rows_out.append({
            "label": label, "variant": variant, "subset": subset, "n": len(rows),
            "ok": ok, "with_timings": len(gen_tps),
            "gen_tps": median(gen_tps), "pre_tps": median(pre_tps),
            "out_tok": median(out_tok), "prompt_tok": median(prompt_tok),
            "gen_s": median(gen_s), "uncached": len(uncached),
            "gen_best": max(gen_tps) if gen_tps else None,
            "pre_best": max(pre_tps) if pre_tps else None,
        })

    head = ("| Run | Variant | n | gen tok/s (best) | gen tok/s (median) | prefill tok/s (best) | uncached reqs | answer tokens | prompt tokens | gen time |\n"
            "|---|---|---|---|---|---|---|---|---|---|")
    lines = [head]
    for r in rows_out:
        def f(v, unit=""):
            return ("%.1f%s" % (v, unit)) if isinstance(v, (int, float)) else "—"
        lines.append("| %s | %s | %d | %s | %s | %s | %d | %s | %s | %s |" % (
            r["label"], r["variant"], r["n"],
            f(r["gen_best"]) if r.get("gen_best") else "—",
            f(r["gen_tps"]),
            f(r["pre_best"]) if r.get("pre_best") else "—",
            r["uncached"],
            ("%d" % r["out_tok"]) if r["out_tok"] else "—",
            ("%d" % r["prompt_tok"]) if r["prompt_tok"] else "—",
            ("%.0f s" % r["gen_s"]) if r["gen_s"] else "—"))
    table = "\n".join(lines)

    header = ("# Performance\n\n"
              "Median server-side numbers per run: generation speed, prefill speed, tokens spent on\n"
              "an answer, prompt size (including the cached prefix) and generation time.\n"
              "These come from the `timings` block of the API response, so queueing and wall-clock\n"
              "noise are excluded. Two speeds are given: **best** (the fastest task, i.e. a run without
"
              "stalls — the figure to quote) and **median** (typical, pulled down by any stall). **Prefill counts only requests that did not hit the prefix cache**\n"
              "(`cache_n = 0`); the column `uncached reqs` says how many samples that is. In a run over\n"
              "one document that is usually one request, since the rest reuse the prefix. Runs made\n"
              "before the fields were captured show “—”.\n\n")
    os.makedirs("docs", exist_ok=True)
    open("docs/performance.md", "w").write(header + table + "\n")
    print(table)


if __name__ == "__main__":
    main()
