#!/usr/bin/env python3
"""Пакетный раннер: все задачи датасета — в одном запросе.

Документ + нумерованный список вопросов; модель должна вернуть JSON вида
{"1": 13, "2": 6, ...}. Ответ разбирается устойчиво: сначала JSON, затем
регулярные пары «номер → число».

Использование:
  python3 run_batch.py --dataset dataset_20k.json --model local-only --out batch_q6.json
"""
import argparse
import json
import re
import time
import urllib.error
import urllib.request

BASE = "http://192.168.1.111:21434"
CLIENT = "openclaw-batch"

INSTRUCTION = (
    "\n\nНиже %d независимых вопросов по этому документу.\n"
    "Ответь ОДНИМ JSON-объектом: ключ — номер вопроса, значение — целое число.\n"
    "Без пояснений, без markdown. Пример: {\"1\": 13, \"2\": -4}\n\n"
)


def build_prompt(document, tasks):
    qs = "\n".join("%d. %s" % (i, t["question"]) for i, t in enumerate(tasks, 1))
    return document + (INSTRUCTION % len(tasks)) + qs + "\n"


def call(prompt, model, max_tokens, timeout=2400):
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(BASE + "/v1/chat/completions", data=body,
                                 headers={"Content-Type": "application/json", "X-Aidir-Client": CLIENT})
    t0 = time.time()
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    except urllib.error.HTTPError as e:
        return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
    except Exception as e:
        return {"error": str(e)[:150], "latency": time.time() - t0}
    ch = (d.get("choices") or [{}])[0]
    msg = ch.get("message") or {}
    return {"content": (msg.get("content") or "").strip(),
            "reasoning_chars": len(msg.get("reasoning_content") or ""),
            "finish": ch.get("finish_reason"),
            "latency": time.time() - t0, "model": d.get("model"),
            "usage": d.get("usage") or {}}


def parse_answers(text, n):
    """JSON, затем регулярные пары. Возвращает {номер: число}."""
    out = {}
    if not text:
        return out
    # 1. JSON-объект
    m = re.search(r"\{.*\}", text, re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            for k, v in obj.items():
                kk = re.search(r"\d+", str(k))
                if kk and isinstance(v, (int, float)):
                    out[int(kk.group(0))] = int(v)
            if out:
                return out
        except Exception:
            pass
    # 2. пары «номер: значение» / «номер — значение»
    for k, v in re.findall(r"(\d{1,2})\s*[:.)\-—]\s*(-?\d+)", text):
        k, v = int(k), int(v)
        if 1 <= k <= n and k not in out:
            out[k] = v
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--out", default="batch_result.json")
    a = ap.parse_args()

    d = json.load(open(a.dataset))
    tasks = d["tasks"]
    prompt = build_prompt(d["document"], tasks)

    print("датасет: %s | модель: %s | задач: %d | max_tokens: %d | промпт: %.0f КБ"
          % (a.dataset, a.model, len(tasks), a.max_tokens, len(prompt.encode()) / 1024))

    out = call(prompt, a.model, a.max_tokens)
    if out.get("error"):
        print("ОШИБКА:", out["error"])
        return

    answers = parse_answers(out["content"], len(tasks))
    rows = []
    for i, t in enumerate(tasks, 1):
        got = answers.get(i)
        rows.append({"num": i, "id": t["id"], "answer": t["answer"], "got": got, "ok": got == t["answer"]})

    ok = sum(1 for r in rows if r["ok"])
    print("ответов разобрано: %d из %d | верно: %d (%.0f%%) | %.1f c | finish=%s"
          % (len(answers), len(tasks), ok, 100.0 * ok / len(tasks), out["latency"], out.get("finish")))
    for r in rows:
        print("  %2d (id %2d) | ожид %5d | получ %s | %s"
              % (r["num"], r["id"], r["answer"], ("%5d" % r["got"]) if r["got"] is not None else "  —",
                 "OK" if r["ok"] else "FAIL"))

    json.dump({"dataset": a.dataset, "model": a.model, "latency_s": round(out["latency"], 1),
               "finish": out.get("finish"), "reasoning_chars": out.get("reasoning_chars"),
               "raw": out["content"][:2000], "rows": rows}, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("файл:", a.out)


if __name__ == "__main__":
    main()
