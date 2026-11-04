#!/usr/bin/env python3
"""Генератор программ для теста 2.

Создаёт Python-программу над массивом из 10 чисел:
  * реальные операции (swap, +=, -=, *=, сортировка срезов, reverse);
  * посторонние присваивания (не меняют arr, но выглядят как код);
  * много комментариев, в том числе с «кодом», который не исполняется;
  * строковые константы-ловушки.

Затем программа запускается, и её настоящий результат сохраняется как эталон.

Пример:
  python3 gen_program.py --seed 7 --ops 10 --comments 400 --extras 120 --traps 40
"""
import argparse
import json
import random
import subprocess
import sys

COMMENT_TOPICS = [
    "проверка граничных значений", "историческая заметка", "черновик", "отладка",
    "ревизия от прошлого квартала", "замечание аналитика", "фрагмент обсуждения",
    "временная пометка", "проверено", "оставлено для совместимости",
]
COMMENT_CODE = [
    "arr[{i}] = {v}", "arr[{i}] += {v}", "arr[{i}] -= {v}", "arr[{i}] *= {v}",
    "arr[{i}], arr[{j}] = arr[{j}], arr[{i}]", "arr[{i}:{j}] = sorted(arr[{i}:{j}])",
]


def gen(seed, ops, comments, extras, traps):
    rng = random.Random(seed)
    arr = [rng.randint(1, 30) for _ in range(10)]
    lines = []

    lines.append('"""Тест 2: вычислить результат выполнения программы."""')
    lines.append("")
    lines.append("# Программа намеренно содержит много комментариев и посторонних присваиваний.")
    lines.append("# Часть строк в комментариях выглядит как код, но не исполняется.")
    lines.append("")

    # блок «документации» с ложным порядком операций
    lines.append("MANUAL = \"\"\"")
    for _ in range(6):
        i, j = rng.randrange(10), rng.randrange(10)
        lines.append(rng.choice(COMMENT_CODE).format(i=i, j=j, v=rng.randint(1, 20)))
    lines.append('"""')
    lines.append("")

    # строки-ловушки
    for t in range(traps):
        i = rng.randrange(10)
        lines.append('TRAP_%d = "arr[%d] = %d"' % (t, i, rng.randint(100, 999)))
    lines.append("")

    lines.append("arr = %r" % arr)
    lines.append("")

    # посторонние присваивания (не влияют на arr)
    for e in range(extras):
        i, j = rng.randrange(10), rng.randrange(10)
        kind = rng.random()
        if kind < 0.5:
            lines.append("tmp_%d = arr[%d] + %d" % (e, i, rng.randint(1, 50)))
        elif kind < 0.8:
            lines.append("note_%d = arr[%d] - arr[%d]" % (e, i, j))
        else:
            lines.append('label_%d = "операция %d не применялась"' % (e, e))

    lines.append("")
    # реальные операции
    real = []
    for k in range(ops):
        kind = rng.random()
        i, j = rng.randrange(10), rng.randrange(10)
        if kind < 0.3:
            lines.append("arr[%d], arr[%d] = arr[%d], arr[%d]" % (i, j, j, i))
            real.append("swap %d/%d" % (i, j))
        elif kind < 0.55:
            v = rng.randint(1, 9)
            lines.append("arr[%d] += %d" % (i, v))
            real.append("arr[%d] += %d" % (i, v))
        elif kind < 0.75:
            v = rng.randint(1, 9)
            lines.append("arr[%d] -= %d" % (i, v))
            real.append("arr[%d] -= %d" % (i, v))
        elif kind < 0.87:
            lines.append("arr[%d] *= 2" % i)
            real.append("arr[%d] *= 2" % i)
        elif kind < 0.95:
            lines.append("arr[%d:%d] = sorted(arr[%d:%d])" % (i, j + 1, i, j + 1) if i < j else "arr[%d] += 1" % i)
            real.append("sort slice")
        else:
            lines.append("arr.reverse()")
            real.append("reverse")

        # между операциями — комментарии
        for _ in range(max(1, comments // max(1, ops))):
            topic = rng.choice(COMMENT_TOPICS)
            if rng.random() < 0.5:
                code = rng.choice(COMMENT_CODE).format(
                    i=rng.randrange(10), j=rng.randrange(10), v=rng.randint(1, 99))
                lines.append("# %s: %s — не выполняется" % (topic, code))
            else:
                lines.append("# %s: строка %d обработана, изменений нет" % (topic, rng.randint(1, 999)))

    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append('    print("ARRAY:", arr)')
    lines.append('    print("SUM:", sum(arr))')
    return "\n".join(lines) + "\n", real


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--ops", type=int, default=10)
    ap.add_argument("--comments", type=int, default=400)
    ap.add_argument("--extras", type=int, default=120)
    ap.add_argument("--traps", type=int, default=40)
    ap.add_argument("--out", default="test2_example_big.py")
    a = ap.parse_args()

    code, real = gen(a.seed, a.ops, a.comments, a.extras, a.traps)
    open(a.out, "w").write(code)

    r = subprocess.run([sys.executable, a.out], capture_output=True, text=True, timeout=60)
    out = r.stdout.strip()
    array = out.split("ARRAY:")[1].split("\n")[0].strip()
    total = out.split("SUM:")[1].strip()

    meta = {"seed": a.seed, "file": a.out, "lines": code.count("\n"),
            "bytes": len(code.encode()), "real_ops": real,
            "expected_array": array, "expected_sum": int(total)}
    json.dump(meta, open(a.out.replace(".py", ".json"), "w"), ensure_ascii=False, indent=1)

    print("файл: %s | строк %d | %.0f КБ | реальных операций %d"
          % (a.out, meta["lines"], meta["bytes"] / 1024, len(real)))
    print("эталон:", array, "| сумма:", total)


if __name__ == "__main__":
    main()
