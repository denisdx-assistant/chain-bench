#!/usr/bin/env python3
"""Генератор v3 для теста 2: вложенные конструкции и второй массив.

Отличия от v2:
  * второй массив arr2 — копия; операции над ним НЕ влияют на arr;
  * функция bump_all с циклом;
  * вложенный if внутри цикла;
  * больше посторонних присваиваний и комментариев (задаётся параметрами).

Сигнатура gen(seed, ops, comments, extras, traps) совпадает с v1/v2.
"""
import random

TOPICS = ["ревизия", "черновик", "отладка", "проверено", "пометка",
          "историческая справка", "замечание аналитика", "временная запись"]
TRAPS = ["arr[{i}] = {v}", "arr[{i}] += {v}", "arr[{i}] *= {v}",
         "arr2[{i}] = {v}", "arr[{i}], arr[{j}] = arr[{j}], arr[{i}]"]


def gen(seed, ops, comments, extras, traps):
    rng = random.Random(seed)
    arr = [rng.randint(1, 30) for _ in range(10)]
    L = []

    L.append('"""Тест 2 v3: исполнить программу и назвать сумму массива arr."""')
    L.append("")
    L.append("def bump_all(a, v):")
    L.append("    for i in range(0, len(a), 2):")
    L.append("        a[i] += v")
    L.append("")
    L.append("def bump_if(a, i, limit, v):")
    L.append("    if a[i] > limit:")
    L.append("        a[i] -= v")
    L.append("    else:")
    L.append("        a[i] += v")
    L.append("")
    L.append("MANUAL = \"\"\"")
    for _ in range(6):
        L.append(rng.choice(TRAPS).format(i=rng.randrange(10), j=rng.randrange(10), v=rng.randint(1, 60)))
    L.append('"""')
    L.append("")

    for t in range(traps):
        L.append('TRAP_%d = "arr[%d] = %d"' % (t, rng.randrange(10), rng.randint(100, 999)))
    L.append("")

    L.append("arr = %r" % arr)
    L.append("arr2 = arr[:]")
    L.append("")

    for e in range(extras):
        i, j = rng.randrange(10), rng.randrange(10)
        k = rng.random()
        if k < 0.35:
            L.append("tmp_%d = arr[%d] + %d" % (e, i, rng.randint(1, 50)))
        elif k < 0.6:
            L.append("note_%d = arr2[%d] - arr[%d]" % (e, i, j))
        elif k < 0.8:
            L.append("copy_%d = arr2[%d]" % (e, i))
        else:
            L.append('label_%d = "запись %d не применялась"' % (e, e))

    L.append("")
    real = []
    for k in range(ops):
        kind = rng.random()
        i, j = rng.randrange(10), rng.randrange(10)
        if kind < 0.15:
            L.append("arr[%d], arr[%d] = arr[%d], arr[%d]" % (i, j, j, i))
            real.append("swap")
        elif kind < 0.3:
            L.append("arr[%d] += %d" % (i, rng.randint(1, 9)))
            real.append("+=")
        elif kind < 0.42:
            L.append("arr[%d] -= %d" % (i, rng.randint(1, 9)))
            real.append("-=")
        elif kind < 0.52:
            L.append("arr[%d] *= 2" % i)
            real.append("*=2")
        elif kind < 0.62:
            L.append("arr[%d:%d] = sorted(arr[%d:%d])" % (i, max(i, j) + 1, i, max(i, j) + 1))
            real.append("sort")
        elif kind < 0.72:
            L.append("bump_all(arr, %d)" % rng.randint(1, 5))
            real.append("bump_all")
        elif kind < 0.82:
            L.append("bump_if(arr, %d, %d, %d)" % (i, rng.randint(5, 25), rng.randint(1, 6)))
            real.append("bump_if")
        elif kind < 0.92:
            L.append("for i in range(0, 10, %d):" % rng.choice([2, 3]))
            L.append("    if arr[i] % 2 == 0:")
            L.append("        arr[i] += %d" % rng.randint(1, 5))
            L.append("    else:")
            L.append("        arr[i] -= %d" % rng.randint(1, 5))
            real.append("loop+if")
        else:
            L.append("arr.reverse()")
            real.append("reverse")

        # шум между операциями
        for _ in range(0 if comments <= 0 else max(1, comments // max(1, ops))):
            if rng.random() < 0.5:
                L.append("# %s: %s — не выполняется" % (
                    rng.choice(TOPICS),
                    rng.choice(TRAPS).format(i=rng.randrange(10), j=rng.randrange(10), v=rng.randint(1, 99))))
            else:
                L.append("# %s: запись %d обработана, изменений нет" % (rng.choice(TOPICS), rng.randint(1, 999)))

    L.append("")
    L.append('if __name__ == "__main__":')
    L.append('    print("ARRAY:", arr)')
    L.append('    print("SUM:", sum(arr))')
    return "\n".join(L) + "\n", real
