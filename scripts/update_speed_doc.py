#!/usr/bin/env python3
"""Replace the table in docs/speed.md with the freshly built one.

The table is the run of lines starting with '|'; everything around it is prose and is
left alone. Replacing by marker beats counting blank lines: an earlier version used
blank-line offsets and silently swallowed the sections that followed the table.
"""
import subprocess
import sys

rows = [l for l in subprocess.run([sys.executable, "scripts/build_speed_table.py"],
                                  capture_output=True, text=True).stdout.splitlines()
        if l.startswith("|")]
if not rows:
    sys.exit("build_speed_table.py produced no table")

path = "docs/speed.md"
lines = open(path).read().splitlines()
out, i, replaced = [], 0, False
while i < len(lines):
    if not replaced and lines[i].startswith("|"):
        while i < len(lines) and lines[i].startswith("|"):
            i += 1
        out.extend(rows)
        replaced = True
        continue
    out.append(lines[i])
    i += 1
if not replaced:
    sys.exit("no table found in docs/speed.md")
open(path, "w").write("\n".join(out) + "\n")
print("docs/speed.md: table replaced with %d rows" % len(rows))
