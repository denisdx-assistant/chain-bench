#!/usr/bin/env python3
"""Генератор датасетов с шумом.

Берёт tasks_final.json и собирает документ: утверждения всех задач в случайном
порядке + шум того же типа + наполнитель. Вопросы задаются отдельно, по одному
на запрос, чтобы ответ был однозначным.

Ключевые правила:
  * имена сущностей из задач в шум не попадают (список запрещённых);
  * шум использует те же предикаты и похожие конструкции;
  * сид фиксируется, датасет воспроизводим.

Пример:
  python3 gen_noise.py --seed 1 --tokens 20000 --noise 300 --out dataset_01
"""
import argparse
import json
import random
import re

NAMES = ["Пётр", "Сергей", "Ганс", "Илья", "Марта", "Олег", "Вера", "Тимур",
         "Нильс", "Роза", "Аркадий", "Лев", "Дина", "Эрик", "Ксения"]
ACTIONS = ["увеличил", "уменьшил", "пересчитал", "проанализировал", "сравнил",
           "перевёл", "объединил", "разделил", "отметил", "отложил"]
BLOCKS = ["журнал", "реестр", "протокол", "сводку", "ведомость", "архив"]
ADJS = ["красный", "серый", "северный", "резервный", "контрольный", "опытный"]

FILLER = ("В документе также приведены общие замечания о порядке согласования, "
          "сроках подготовки и составе участников. Отмечено, что часть записей "
          "относится к прошлым периодам и не влияет на текущие расчёты. ")

ENTITY = re.compile(r"[А-Яа-яЁёA-Za-z]+-\d+")


def forbidden_names(tasks):
    names = set()
    for t in tasks:
        for s in t["statements"]:
            names.update(ENTITY.findall(s))
    return names


def noise_line(rng, banned):
    kind = rng.random()
    name = rng.choice(NAMES)
    if name in banned:
        return None
    obj = "variable%d" % rng.randint(10, 999)
    if kind < 0.35:
        return "%s %s %s на %d единиц." % (name, rng.choice(ACTIONS), obj, rng.randint(1, 40))
    if kind < 0.6:
        return "%s %s и записал результат в %s." % (name, rng.choice(ACTIONS), rng.choice(BLOCKS))
    if kind < 0.8:
        return ("Показатель %s превышает норму на %d процентов и помечен как %s."
                % (obj, rng.randint(1, 25), rng.choice(ADJS)))
    if kind < 0.9:
        return "Все объекты с индексами, кратными %d, считаются %s." % (rng.randint(3, 9), rng.choice(ADJS))
    # почти-двойник номера: та же сущность с переставленными цифрами
    m = re.search(r"(\d{2})", obj)
    if m:
        n = m.group(1)
        swapped = n[::-1] if n[::-1] != n else str(int(n) + 1)
        return "Запись %s-%s относится к другому набору и не учитывается." % ("объект", swapped)
    return None


def build(tasks, seed, tokens, noise_count):
    rng = random.Random(seed)
    banned = forbidden_names(tasks)

    statements = []
    for t in tasks:
        statements.extend(t["statements"])
    rng.shuffle(statements)

    noise = []
    guard = 0
    while len(noise) < noise_count and guard < noise_count * 20:
        guard += 1
        line = noise_line(rng, banned)
        if line:
            noise.append(line)

    body = statements + noise
    rng.shuffle(body)

    text = "\n".join(body)
    need = max(0, int(tokens * 3.6) - len(text))
    filler = (FILLER * (need // len(FILLER) + 1))[:need]

    # наполнитель расставляем до и после, чтобы цепочки не оказались в хвосте
    half = len(filler) // 2
    document = filler[:half] + "\n\n" + text + "\n\n" + filler[half:]
    return document, len(noise)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="tasks_final.json")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tokens", type=int, default=20000)
    ap.add_argument("--noise", type=int, default=300)
    ap.add_argument("--out", default="dataset_01")
    ap.add_argument("--example", action="store_true")
    a = ap.parse_args()

    tasks = json.load(open(a.tasks))
    document, n_noise = build(tasks, a.seed, a.tokens, a.noise)

    payload = {"seed": a.seed, "tokens_target": a.tokens, "noise_lines": n_noise,
               "document": document,
               "tasks": [{"id": t["id"], "question": t["question"], "answer": t["answer"]} for t in tasks]}
    json.dump(payload, open(a.out + ".json", "w"), ensure_ascii=False, indent=1)

    with open(a.out + ".md", "w") as f:
        f.write("# Датасет %s\n\n" % a.out)
        f.write("> сид %d · объём ~%d токенов · шумовых строк %d · задач %d\n\n"
                % (a.seed, a.tokens, n_noise, len(tasks)))
        f.write("## Документ\n\n```\n%s\n```\n\n" % document)
        f.write("## Вопросы\n\n")
        for t in tasks:
            f.write("- **%d.** %s  \n  *эталон: `%d`*\n" % (t["id"], t["question"], t["answer"]))

    if a.example:
        t0 = tasks[0]
        with open("example_request.md", "w") as f:
            f.write("# Пример запроса (с шумом)\n\n")
            f.write("> Файлы: [[dataset_example.json]] · генератор [[gen_noise.py]] · задачи [[tasks_final.md]]\n\n")
            f.write("> сид %d · объём ~%d токенов · шумовых строк %d\n\n" % (a.seed, a.tokens, n_noise))
            f.write("Запрос к модели состоит из документа и одного вопроса:\n\n")
            f.write("```\nДОКУМЕНТ\n%s\n\nВОПРОС: %s\n```\n" % (document[:3000] + "\n…(документ продолжается)…", t0["question"]))
            f.write("\nЭталон: `%d`\n" % t0["answer"])

    print("датасет %s: шум %d строк, задач %d, объём %.0f КБ"
          % (a.out, n_noise, len(tasks), len(document.encode()) / 1024))
    if a.example:
        print("пример: example_request.md")


if __name__ == "__main__":
    main()
