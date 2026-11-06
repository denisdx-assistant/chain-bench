#!/usr/bin/env python3
"""Collect context-length measurements into docs/context-prefill.md."""
import glob
import json
import os

def main():
    rows = []
    for p in sorted(glob.glob("results/context/*/report.json")):
        d = json.load(open(p))
        rows.append(d)
    rows.sort(key=lambda d: (str(d.get("resolved_provider")), d.get("prompt_tokens") or 0))
    head = ("| Model (provider) | Target | Prompt tokens | Prefill tok/s | Prefill time | Answer tokens | Gen tok/s | Wall | Count |\n"
            "|---|---|---|---|---|---|---|---|---|")
    lines = [head]
    for d in rows:
        prov = (d.get("resolved_provider") or "—").replace("local_", "")
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            prov, d.get("label") or "—",
            d.get("prompt_tokens") or "—",
            d.get("prefill_tps") or "—",
            ("%.0f s" % (d["prefill_ms"] / 1000)) if d.get("prefill_ms") else "—",
            d.get("answer_tokens") or "—",
            d.get("gen_tps") or "—",
            ("%.0f s" % d["wall_s"]) if d.get("wall_s") else "—",
            "✓" if d.get("correct") else "✗"))
    table = "\n".join(lines)
    header = ("# Context-length prefill\n\n"
              "Measured with `scripts/context_count.py`: one long prompt of filler words, a word-count\n"
              "question, and the server's own timings. Prompt size is the actual token count reported by\n"
              "the server, not the requested one. Prefill speed is the mean over the whole prompt, so it\n"
              "rises with context length and should be compared at equal sizes.\n\n")
    os.makedirs("docs", exist_ok=True)
    open("docs/context-prefill.md", "w").write(header + table + "\n")
    print(table)

if __name__ == "__main__":
    main()
