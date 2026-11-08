#!/usr/bin/env python3
"""Measured speed per model, bucketed by total prompt size.

Source: server timings stored with every result row. Prefill speed is taken only
from requests with an empty prompt cache (cache_n == 0); a cached request reports
the speed of the few uncached tokens, which is not comparable.
"""
import glob, json, os, statistics
from collections import defaultdict

BUCKETS = [("5k", 0, 8000), ("20k", 8000, 32000), ("60k", 32000, 100000),
           ("150k", 100000, 250000), ("250k+", 250000, 10 ** 9)]


def configs():
    try:
        return json.load(open("results/run-configs.json"))
    except Exception:
        return {}


def note_for(folder, cfg):
    hosts = {v.get("host") or "" for k, v in cfg.items() if k.startswith(folder + "/")}
    hosts = {h for h in hosts if h}
    notes = []
    if hosts:
        notes.append(sorted(hosts)[0])
    if any("1 GPU" in (v.get("note") or "") for k, v in cfg.items() if k.startswith(folder + "/")):
        notes.append("single GPU")
    return ", ".join(notes) or "—"


def main():
    cfg = configs()
    acc = defaultdict(lambda: defaultdict(lambda: {"pre": [], "gen": [], "tok": []}))
    for path in sorted(glob.glob("results/*/*.json")):
        if any(x in path for x in ("_retries", "_archive", "_invalid")):
            continue
        folder = path.split("/")[1]
        try:
            d = json.load(open(path))
        except Exception:
            continue
        rows = d if isinstance(d, list) else (d.get("rows") or [])
        for r in rows:
            if not isinstance(r, dict):
                continue
            st = r.get("server_timings") or {}
            if not isinstance(st, dict):
                continue
            pn = st.get("prompt_n")
            if not pn:
                continue
            total = pn + (st.get("cache_n") or 0)
            for name, lo, hi in BUCKETS:
                if lo <= total < hi:
                    if st.get("prompt_per_second") and (st.get("cache_n") or 0) == 0:
                        acc[folder][name]["pre"].append(st["prompt_per_second"])
                    if st.get("predicted_per_second"):
                        acc[folder][name]["gen"].append(st["predicted_per_second"])
                    if st.get("predicted_n"):
                        acc[folder][name]["tok"].append(st["predicted_n"])
                    break

    probes = {}
    for p in glob.glob("results/_speed/*.json"):
        name = os.path.basename(p)[:-5]
        try:
            probes[name] = json.load(open(p))
        except Exception:
            pass

    def probe_cell(folder, want_kind, want):
        for rec in probes.get(folder) or []:
            if rec.get("want") == want:
                if want_kind == "pre" and rec.get("prompt_tps"):
                    return "%d t/s" % round(rec["prompt_tps"])
                if want_kind == "gen" and rec.get("gen_tps"):
                    return "%d t/s" % round(rec["gen_tps"])
        return "—"

    def med(xs):
        return int(round(statistics.median(xs))) if xs else None

    head = ("| Model | Prefill 5k | Prefill 20k | Prefill 60k | Prefill 150k | Prefill 250k | Prefill 500k | "
            "Prefill 1M | Gen 5k | Gen 20k | Gen 60k | Gen 150k | Gen 250k | Gen 500k | Gen 1M | Tokens/task | Notes |")
    sep = "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"
    lines = [head, sep]
    for folder in sorted(acc):
        cells = []
        for name, _, _ in BUCKETS[:4]:
            v = med(acc[folder][name]["pre"])
            cells.append("%s t/s" % v if v else "—")
        for want in (250000, 500000, 1000000):
            cells.append(probe_cell(folder, "pre", want))
        for name, _, _ in BUCKETS[:4]:
            v = med(acc[folder][name]["gen"])
            cells.append("%s t/s" % v if v else "—")
        for want in (250000, 500000, 1000000):
            cells.append(probe_cell(folder, "gen", want))
        alltok = [t for name, _, _ in BUCKETS for t in acc[folder][name]["tok"]]
        cells.append(str(med(alltok)) if alltok else "—")
        cells.append(note_for(folder, cfg))
        lines.append("| %s | %s |" % (folder, " | ".join(cells)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
