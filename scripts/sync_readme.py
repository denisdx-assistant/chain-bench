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

# generated prose and table headers, per language; the data rows are identical everywhere
HEAD = ("| Run | Overall (errors) | Median tokens/task | Test 1 en (correct) | Test 1 ru (correct) | "
        "Test 1 zh (correct) | Test 1 subsets 8 (all langs) | Test 2 (correct) |")
FOOT = ("⚠ — not every task was computed for this row (missing sets, a short file, or tasks left "
        "unresolved): its quality percentages are not comparable with the others.")

LOCALE = {
    "README.ru.md": {
        "head": ("| Прогон | Итог (ошибки) | Медиана токенов на задачу | Тест 1 en (верно) | "
                 "Тест 1 ru (верно) | Тест 1 zh (верно) | Тест 1 подмножества 8 (все языки) | "
                 "Тест 2 (верно) |"),
        "foot": ("⚠ — не все задачи этой строки просчитаны (нет части наборов, файл неполный или "
                 "есть несостоявшиеся задачи): проценты качества несравнимы с остальными строками."),
        "of_run": "из %d",
        "subs": [("% err", " ош."), (" of 20 run", " из 20"),
                 ("(ru/zh only)", "(только ru/zh)"), ("unresolved ", "не посчитано ")],
    },
    "README.zh.md": {
        "head": ("| 运行 | 总计（错误） | 每题中位 token 数 | 测试 1 en（正确） | 测试 1 ru（正确） | "
                 "测试 1 zh（正确） | 测试 1 子集 8（全部语言） | 测试 2（正确） |"),
        "foot": ("⚠ — 该行并非所有题目都已计算（缺少部分集合、文件不完整或存在未完成题目）："
                 "其质量百分比无法与其他行比较。"),
        "of_run": "%d 题中",
        "subs": [("% err", "% 错误"), (" of 20 run", " / 20"),
                 ("(ru/zh only)", "（仅 ru/zh）"), ("unresolved ", "未完成 ")],
    },
}


def localize(block, path):
    loc = LOCALE.get(path)
    if not loc:
        return block
    out = block.replace(HEAD, loc["head"]).replace(FOOT, loc["foot"])
    for a, b in loc.get("subs", []):
        out = out.replace(a, b)
    return out
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
    for path in READMES:
        new = START + "\n" + localize(block, path) + "\n" + END
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
