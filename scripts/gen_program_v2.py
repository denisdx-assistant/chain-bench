#!/usr/bin/env python3
"""Генератор v2 для теста 2: управляющие конструкции.

Дополнительно к v1:
  * if/else, влияющие на массив в зависимости от условия;
  * цикл for с шагом;
  * вызов функции, которая меняет массив;
  * второй массив-копия, операции над которым НЕ влияют на arr;
  * ловушки в комментариях, строках и документации.

Сигнатура gen(seed, ops, comments, extras, traps) совпадает с v1,
поэтому run_programs.py может использовать любой вариант.
"""
import random

COMMENT_TOPICS = ["историческая заметка", "черновик", "отладка", "ревизия",
                  "замечание аналитика", "временная пометка", "проверено"]
TRAP_CODE = ["arr[{i}] = {v}", "arr[{i}] += {v}", "arr[{i}] *= {v}",
             "arr[{i}], arr[{j}] = arr[{j}], arr[{i}]"]


def gen(seed, ops, comments, extras, traps):
    rng = random.Random(seed)
    arr = [rng.randint(1, 30) for _ in range(10)]
    lines = []

    lines.append('"""Тест 2 v2: исполнить программу и назвать сумму массива."""')
    lines.append("")
    lines.append("def bump(a, i, v):")
    lines.append("    a[i] += v")
    lines.append("")
    lines.append("MANUAL = \"\"\"")
    for _ in range(5):
        lines.append(rng.choice(TRAP_CODE).format(i=rng.randrange(10), j=rng.randrange(10), v=rng.randint(1, 50)))
    lines.append('"""')
    lines.append("")

    for t in range(traps):
        lines.append('TRAP_%d = "arr[%d] = %d"' % (t, rng.randrange(10), rng.randint(100, 999)))
    lines.append("")

    lines.append("arr = %r" % arr)
    lines.append("arr_copy = arr[:]")
    lines.append("")

    for e in range(extras):
        i, j = rng.randrange(10), rng.randrange(10)
        k = rng.random()
        if k < 0.4:
            lines.append("tmp_%d = arr[%d] + %d" % (e, i, rng.randint(1, 50)))
        elif k < 0.7:
            lines.append("note_%d = arr_copy[%d] - arr[%d]" % (e, i, j))
        else:
            lines.append('label_%d = "операция %d не применялась"' % (e, e))

    lines.append("")
    real = []
    for k in range(ops):
        kind = rng.random()
        i, j = rng.randrange(10), rng.randrange(10)
        if kind < 0.18:
            lines.append("arr[%d], arr[%d] = arr[%d], arr[%d]" % (i, j, j, i))
            real.append("swap")
        elif kind < 0.34:
            v = rng.randint(1, 9)
            lines.append("arr[%d] += %d" % (i, v))
            real.append("+=")
        elif kind < 0.46:
            v = rng.randint(1, 9)
            lines.append("arr[%d] -= %d" % (i, v))
            real.append("-=")
        elif kind < 0.56:
            lines.append("arr[%d] *= 2" % i)
            real.append("*=2")
        elif kind < 0.66:
            lines.append("arr[%d:%d] = sorted(arr[%d:%d])" % (i, max(i, j) + 1, i, max(i, j) + 1))
            real.append("sort")
        elif kind < 0.76:
            lines.append("bump(arr, %d, %d)" % (i, rng.randint(1, 7)))
            real.append("bump")
        elif kind < 0.86:
            t = rng.randint(1, 20)
            lines.append("if arr[%d] > %d:" % (i, t))
            lines.append("    arr[%d] += %d" % (j, rng.randint(1, 9)))
            lines.append("else:")
            lines.append("    arr[%d] -= %d" % (j, rng.randint(1, 9)))
            real.append("if/else")
        elif kind < 0.94:
            step = rng.choice([2, 3])
            v = rng.randint(1, 5)
            lines.append("for i in range(0, 10, %d):" % step)
            lines.append("    arr[i] += %d" % v)
            real.append("loop")
        else:
            lines.append("arr.reverse()")
            real.append("reverse")

        for _ in range(max(1, comments // max(1, ops))):
            topic = rng.choice(COMMENT_TOPICS)
            if rng.random() < 0.5:
                lines.append("# %s: %s — не выполняется" % (
                    topic, rng.choice(TRAP_CODE).format(i=rng.randrange(10), j=rng.randrange(10), v=rng.randint(1, 99))))
            else:
                lines.append("# %s: запись %d обработана, изменений нет" % (topic, rng.randint(1, 999)))

    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append('    print("ARRAY:", arr)')
    lines.append('    print("SUM:", sum(arr))')
    return "\n".join(lines) + "\n", real
