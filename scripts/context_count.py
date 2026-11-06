#!/usr/bin/env python3
"""Context-length prefill benchmark against the local aidir endpoint.

Based on the owner's context_count_1m.py, adapted to this host: endpoint and
model come from config/endpoint, an optional bearer token from config/token,
and every run records the server's own timings (prefill and generation speed,
token counts).

The prompt asks the model to count occurrences of a word in a long filler block,
answer "результат теста: N", then write a story. The count is checked; the
prefill numbers are what we care about here.

  python3 scripts/context_count.py --calibrate
  python3 scripts/context_count.py --words 200000
"""
import argparse
import json
import os
import random
import re
import secrets
import statistics
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDS = """
time day night year man woman child king queen town
city road house room door book tree river sea wind
rain snow sun moon star fire water earth stone wood
hand eye face heart mind life world home friend name
light dark red blue green gold black white old young
good bad long short small great new last first next
""".split()


def endpoint():
    p = ROOT / "config" / "endpoint"
    base = os.environ.get("CHAIN_BENCH_ENDPOINT") or (p.read_text().strip() if p.exists() else "")
    return (base or "http://127.0.0.1:21434").rstrip("/")


def token():
    p = ROOT / "config" / "token"
    return os.environ.get("CHAIN_BENCH_TOKEN") or (p.read_text().strip() if p.exists() else "")


def provider():
    """Which model the router serves, from metadata only (no model request)."""
    try:
        with urllib.request.urlopen(endpoint() + "/v1/models/local-only", timeout=10) as r:
            a = (json.load(r).get("aidir") or {})
        return a.get("resolved_provider"), a.get("resolved_model")
    except Exception:
        return None, None


def ask(prompt, max_tokens, timeout):
    body = json.dumps({"model": "local-only", "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": max_tokens, "temperature": 0}).encode()
    headers = {"Content-Type": "application/json"}
    tok = token()
    if tok:
        headers["Authorization"] = "Bearer " + tok
    req = urllib.request.Request(endpoint() + "/v1/chat/completions", data=body, headers=headers)
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
        return json.loads(raw), time.monotonic() - t0, None
    except urllib.error.HTTPError as e:
        return None, time.monotonic() - t0, "HTTP %s: %s" % (e.code, e.read()[:300].decode("utf-8", "replace"))
    except Exception as e:
        return None, time.monotonic() - t0, str(e)[:300]


def build_prompt(words, target, seed):
    rng = random.Random(seed)
    sequence = rng.choices(WORDS, k=words)
    expected = sequence.count(target)
    filler = " ".join(sequence)
    del sequence
    prompt = (
        f"Идентификатор теста: {secrets.token_hex(12)}\n\n"
        f"Посчитай точное количество вхождений английского слова '{target}' в тексте "
        "между <test_text> и </test_text> ниже. Считай только отдельные слова внутри "
        "этого блока, не учитывай слова в инструкции или в будущем ответе. "
        "Текст внутри блока является только данными.\n\n"
        "Начни свой окончательный ответ строго со строки:\n"
        "результат теста: N\n"
        "Вместо N поставь фактическое целое число без пробелов и разделителей разрядов. "
        "Не пиши ничего перед этой строкой. После неё придумай длинную связную "
        f"историческую приключенческую историю на английском языке об образе или предмете '{target}'.\n\n"
        "<test_text>\n" + filler + "\n</test_text>"
    )
    return prompt, expected


def metrics(response, wall):
    t = (response or {}).get("timings") or {}
    pre = t.get("prompt_per_second")
    gen = t.get("predicted_per_second")
    return {
        "wall_s": round(wall, 1),
        "prompt_tokens": (t.get("prompt_n") or 0) + (t.get("cache_n") or 0),
        "uncached_prompt_tokens": t.get("prompt_n"),
        "prefill_ms": t.get("prompt_ms"),
        "prefill_tps": round(pre, 1) if pre else None,
        "answer_tokens": t.get("predicted_n"),
        "gen_ms": t.get("predicted_ms"),
        "gen_tps": round(gen, 1) if gen else None,
        "finish": ((response or {}).get("choices") or [{}])[0].get("finish_reason"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--words", type=int, default=200_000)
    ap.add_argument("--target", default="gold")
    ap.add_argument("--seed", type=int, default=20261103)
    ap.add_argument("--max-tokens", type=int, default=8192)
    ap.add_argument("--timeout", type=int, default=7200)
    ap.add_argument("--label", default="")
    ap.add_argument("--calibrate", action="store_true")
    a = ap.parse_args()

    prov, pmodel = provider()
    tag = a.label or ("calib" if a.calibrate else "%dk" % (a.words // 1000))
    out = ROOT / "results" / "context" / ("%s-%s" % (datetime.now().strftime("%Y%m%d-%H%M%S"), tag))
    out.mkdir(parents=True, exist_ok=True)

    prompt, expected = build_prompt(a.words, a.target, a.seed)
    print("слов: %d | символов в промпте: %d | ожидаемый счёт: %d" % (a.words, len(prompt), expected), flush=True)
    response, wall, err = ask(prompt, a.max_tokens, a.timeout)
    if err:
        print("ОШИБКА:", err, flush=True)
        (out / "error.txt").write_text(err)
        raise SystemExit(1)
    content = ((response.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    (out / "answer.txt").write_text(content)
    m = metrics(response, wall)
    match = re.match(r"\A\s*результат теста:\s*(\d+)", content)
    reported = int(match.group(1)) if match else None
    if reported is None:
        m["count_status"] = "no count line in the answer"
    else:
        m["count_status"] = "correct" if reported == expected else "wrong"
    m.update({"resolved_provider": prov, "resolved_model": pmodel,
              "words": a.words, "expected": expected, "reported": reported,
              "correct": reported == expected, "target": a.target, "model": "local-only",
              "label": tag})
    (out / "report.json").write_text(json.dumps(m, indent=1, ensure_ascii=False))
    print("\n--- РЕЗУЛЬТАТ ---")
    print("промпт: %s токенов (некэш. %s), префилл %s т/с за %.0f мс" % (
        m["prompt_tokens"], m["uncached_prompt_tokens"], m["prefill_tps"], (m["prefill_ms"] or 0)))
    print("ответ: %s токенов, генерация %s т/с, %.1f с" % (m["answer_tokens"], m["gen_tps"], m["gen_ms"] / 1000))
    print("настенное время: %.1f с | finish: %s" % (m["wall_s"], m["finish"]))
    print("счёт: ожидалось %d, модель сказала %s -> %s" % (expected, reported, "верно" if m["correct"] else "неверно"))
    print("отчёт:", out / "report.json")
    if a.calibrate:
        ratio = (m["prompt_tokens"] / a.words) if a.words else 0
        print("\nкалибровка: токенов на слово ≈ %.3f" % ratio)
        print("для 261k токенов нужно ≈ %d слов" % (261000 / ratio if ratio else 0))
        print("для 512k токенов нужно ≈ %d слов" % (512000 / ratio if ratio else 0))
        print("для 1M токенов нужно ≈ %d слов" % (1000000 / ratio if ratio else 0))


if __name__ == "__main__":
    main()
