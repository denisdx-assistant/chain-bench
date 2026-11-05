#!/usr/bin/env python3
"""Refresh generated content.

1. `scripts/build_task_tables.py` rewrites `docs/results-by-task.md` with the
   per-task matrices.
2. The summary table is spliced into README.md between the summary markers.

Everything outside the markers is hand-written and never touched.
"""
import subprocess
import sys

READMES = ["README.md", "README.ru.md", "README.zh.md"]
START = "<!-- summary:start -->"
END = "<!-- summary:end -->"


def main():
    # per-task detail document
    subprocess.run([sys.executable, "scripts/build_task_tables.py"],
                   capture_output=True, text=True, check=True)
    # summary table for the README
    block = subprocess.run([sys.executable, "scripts/build_task_tables.py", "--summary"],
                           capture_output=True, text=True, check=True).stdout.strip()

    changed = []
    new = START + "\n" + block + "\n" + END
    for path in READMES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if START not in text or END not in text:
            print("markers missing in", path)
            continue
        i = text.index(START)
        j = text.index(END) + len(END)
        updated = text[:i] + new + text[j:]
        if updated != text:
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated)
            changed.append(path)
    print("updated: " + ", ".join(changed) if changed else "unchanged")


if __name__ == "__main__":
    main()
