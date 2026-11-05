#!/usr/bin/env python3
"""Regenerate the summary and per-task tables and splice them into README.md.

The block between <!-- per-task:start --> and <!-- per-task:end --> is fully
generated; everything outside it is hand-written and never touched.
Exit code 0 always; prints whether the README changed.
"""
import subprocess
import sys

README = "README.md"
START = "<!-- per-task:start -->"
END = "<!-- per-task:end -->"

HEADER = """## 6.5 Summary and per-task results

The first table is the summary: one row per run configuration, one column per
test group, each cell is the total wall-clock time of that series and its score.
A model may appear in several rows when it was served with a different context,
YaRN setting, temperature or budget; the row label carries the configuration.
The tables below give the same runs task by task.
Everything here is generated from the result files and `results/run-configs.json`
by `scripts/build_task_tables.py`; do not edit by hand.
"""


def main():
    block = subprocess.run([sys.executable, "scripts/build_task_tables.py"],
                           capture_output=True, text=True, check=True).stdout.strip()
    with open(README, encoding="utf-8") as f:
        text = f.read()
    new = START + "\n" + HEADER + "\n" + block + "\n\n" + END
    if START in text and END in text:
        i = text.index(START)
        j = text.index(END) + len(END)
        updated = text[:i] + new + text[j:]
    else:
        anchor = "## 7. Qualitative comparison"
        updated = text.replace(anchor, new + "\n\n" + anchor, 1)
    if updated == text:
        print("unchanged")
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)
    print("updated")


if __name__ == "__main__":
    main()
