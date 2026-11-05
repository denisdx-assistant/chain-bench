#!/usr/bin/env python3
"""Раннер теста 1: прогоняет датасет через модель и считает точность.

Особенности:
  * бюджет по умолчанию 6000 токенов — у Q6 длинный reasoning;
  * если ответ пустой и finish_reason=length, делается один повтор с большим бюджетом;
  * фиксируется finish_reason и длина reasoning, чтобы отличать ошибку модели от обрыва.

Использование:
  python3 run_chains.py --dataset dataset_20k.json --model local-only --out calib_q6.json
  python3 run_chains.py --dataset dataset_20k.json --model local-only --limit 5
"""
import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "endpoint")
BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or (open(_cfg).read().strip() if os.path.exists(_cfg) else "")
        or "http://127.0.0.1:21434")


def call(document, question, model, max_tokens, timeout=2400):
    prompt = document + "\n\nВопрос: " + question
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(BASE + "/v1/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "X-Aidir-Client": "openclaw-chain"})
    t0 = time.time()
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    except urllib.error.HTTPError as e:
        return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
    except Exception as e:
        return {"error": str(e)[:120], "latency": time.time() - t0}
    ch = (d.get("choices") or [{}])[0]
    msg = ch.get("message") or {}
    return {"content": (msg.get("content") or "").strip(),
            "reasoning_chars": len(msg.get("reasoning_content") or ""),
            "finish": ch.get("finish_reason"),
            "latency": time.time() - t0, "model": d.get("model"),
            "usage": d.get("usage") or {}}


def parse_int(text):
    m = re.search(r"-?\d+", (text or "").replace("−", "-"))
    return int(m.group(0)) if m else None


def ask(document, question, model, max_tokens):
    out = call(document, question, model, max_tokens)
    retried = False
    if not out.get("error") and not out.get("content") and out.get("finish") == "length":
        bigger = min(32000, max_tokens * 2)
        out2 = call(document, question, model, bigger)
        out2["retried_from"] = max_tokens
        out2["latency"] = out["latency"] + out2.get("latency", 0)
        retried = True
        out = out2
    out["retried"] = retried
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--out", default="run_result.json")
    a = ap.parse_args()

    d = json.load(open(a.dataset))
    document = d["document"]
    tasks = d["tasks"]
    if a.limit:
        tasks = tasks[:a.limit]

    print("датасет: %s | модель: %s | задач: %d | объём: %.0f КБ | max_tokens: %d"
          % (a.dataset, a.model, len(tasks), len(document.encode()) / 1024, a.max_tokens))

    rows = []
    for t in tasks:
        out = ask(document, t["question"], a.model, a.max_tokens)
        got = parse_int(out.get("content"))
        empty = (got is None and not out.get("error"))
        ok = (got == t["answer"])
        rows.append({"id": t["id"], "answer": t["answer"], "got": got, "ok": ok,
                     "empty": empty, "finish": out.get("finish"),
                     "retried": out.get("retried"), "reasoning_chars": out.get("reasoning_chars"),
                     "latency_s": round(out.get("latency", 0), 1),
                     "model": out.get("model"), "error": out.get("error"),
                     "raw": (out.get("content") or "")[:120]})
        print("  %2d | ожидалось %5d | получено %s | %s | %s%s | %5.1f c"
              % (t["id"], t["answer"], ("%5d" % got) if got is not None else "    —",
                 "OK" if ok else "FAIL",
                 "empty " if empty else "", "retry " if out.get("retried") else "",
                 out.get("latency", 0)))

    ok_n = sum(1 for r in rows if r["ok"])
    empty_n = sum(1 for r in rows if r["empty"])
    err_n = sum(1 for r in rows if r["error"])
    print("\nИТОГ: %d/%d верно (%.0f%%) | пустых %d | ошибок запросов %d"
          % (ok_n, len(rows), 100.0 * ok_n / max(1, len(rows)), empty_n, err_n))

    json.dump({"dataset": a.dataset, "model": a.model, "rows": rows}, open(a.out, "w"),
              ensure_ascii=False, indent=1)
    print("файл:", a.out)


if __name__ == "__main__":
    main()
