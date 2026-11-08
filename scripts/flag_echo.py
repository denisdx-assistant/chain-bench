#!/usr/bin/env python3
"""Mark probe records where the model re-quoted the prompt instead of writing the story.

A reply that reproduces the source is generated from text the model has just read, so
draft/MTP decoding accepts almost every token: its tokens/second says nothing about
writing speed. Prefill is measured before generation starts, so those points keep their
prefill number and lose only the generation one.

The signal is the instruction: it asks for the last ten words first, so a genuine answer
opens with that line. Anything else is treated as an echo.

Usage: python3 scripts/flag_echo.py [--write]
"""
import glob
import json
import os
import sys

def _cyrillic_ratio(text):
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for c in letters if "\u0400" <= c <= "\u04ff") / len(letters)


def classify(rec):
    """A story is written in Russian, because the instruction is Russian and asks for one.

    The filler, by contrast, is a stream of English dictionary words. So a reply with
    almost no Cyrillic is the source being quoted back, not a story.
    """
    head = str(rec.get("answer_head") or rec.get("story_head") or "").strip()
    if not head:
        # nothing to inspect: the run wrote no visible answer, so it cannot measure writing
        return "echo"
    # complying with the instruction is proof enough: it opens with the tail words
    if head.lower().startswith(("последние 10 слов", "last ten words", "last 10 words")):
        return "genuine"
    ratio = _cyrillic_ratio(head)
    if ratio >= 0.2:
        return "genuine"
    if ratio < 0.05:
        return "echo"
    return "unknown"


def main():
    write = "--write" in sys.argv
    changed = 0
    for path in sorted(glob.glob("results/_speed*/*.json")):
        try:
            recs = json.load(open(path))
        except Exception:
            continue
        dirty = False
        for rec in recs:
            kind = classify(rec)
            if rec.get("echo") != (kind == "echo"):
                rec["echo"] = (kind == "echo")
                rec["echo_check"] = kind
                dirty, changed = True, changed + 1
        if dirty:
            print("%-58s %s" % (os.path.basename(path),
                                ", ".join("%s=%s" % (r.get("want"), r.get("echo_check")) for r in recs)))
            if write:
                json.dump(recs, open(path, "w"), ensure_ascii=False, indent=1)
    print("%d record(s) updated%s" % (changed, "" if write else " (dry run, pass --write)"))


if __name__ == "__main__":
    main()
