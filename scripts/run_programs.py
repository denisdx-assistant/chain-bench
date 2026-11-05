#!/usr/bin/env python3
"""Раннер теста 2: программы с шумом.

Для каждой программы:
  1. генерируется код (реальные операции + посторонние присваивания + комментарии-ловушки);
  2. программа запускается локально — так получается эталон;
  3. модель получает текст программы и вопрос о сумме массива;
  4. ответ сравнивается с эталоном.

Использование:
  python3 run_programs.py --model local-only --n 10 --ops 8 --comments 300 --extras 100 --traps 30
  python3 run_programs.py --model local-only --n 5 --ops 15 --comments 800 --extras 300 --traps 80
"""
import argparse
import importlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

from gen_program import gen

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "endpoint")
BASE = (os.environ.get("CHAIN_BENCH_ENDPOINT")
        or (open(_cfg).read().strip() if os.path.exists(_cfg) else "")
        or "http://127.0.0.1:21434")
CLIENT = "openclaw-programs"

QUESTION = ("\n\nВопрос: чему равна сумма элементов массива arr после выполнения этой программы? "
            "Ответь одним целым числом.")


def run_program(code):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name
    r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=120)
    out = r.stdout
    arr = out.split("ARRAY:")[1].split("\n")[0].strip()
    total = int(out.split("SUM:")[1].strip())
    return arr, total


def ask(code, model, max_tokens=16000, timeout=2400):
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": code + QUESTION}]}).encode()
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
            "latency": time.time() - t0, "model": d.get("model")}


def parse_int(text):
    m = re.search(r"-?\d+", (text or "").replace("−", "-"))
    return int(m.group(0)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--ops", type=int, default=8)
    ap.add_argument("--comments", type=int, default=300)
    ap.add_argument("--extras", type=int, default=100)
    ap.add_argument("--traps", type=int, default=30)
    ap.add_argument("--seed", type=int, default=100)
    ap.add_argument("--gen", default="gen_program", help="модуль генератора: gen_program или gen_program_v2")
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--out", default="programs_result.json")
    a = ap.parse_args()
    gen = importlib.import_module(a.gen).gen

    print("модель: %s | программ: %d | ops=%d comments=%d extras=%d traps=%d"
          % (a.model, a.n, a.ops, a.comments, a.extras, a.traps))

    rows = []
    for i in range(a.n):
        seed = a.seed + i
        code, real_ops = gen(seed, a.ops, a.comments, a.extras, a.traps)
        arr, total = run_program(code)
        out = ask(code, a.model, a.max_tokens)
        got = parse_int(out.get("content"))
        ok = (got == total)
        rows.append({"seed": seed, "lines": code.count("\n"), "expected": total,
                     "expected_array": arr, "got": got, "ok": ok,
                     "latency_s": round(out.get("latency", 0), 1),
                     "reasoning_chars": out.get("reasoning_chars"),
                     "finish": out.get("finish"), "error": out.get("error"),
                     "raw": (out.get("content") or "")[:120]})
        print("  %2d | строк %4d | эталон %5d | получено %s | %s | %5.1f c"
              % (i + 1, code.count("\n"), total,
                 ("%5d" % got) if got is not None else "    —",
                 "OK" if ok else "FAIL", out.get("latency", 0)))

    ok_n = sum(1 for r in rows if r["ok"])
    print("\nИТОГ: %d/%d верно (%.0f%% ошибок)" % (ok_n, len(rows), 100.0 * (len(rows) - ok_n) / len(rows)))
    json.dump(rows, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("файл:", a.out)


if __name__ == "__main__":
    main()
