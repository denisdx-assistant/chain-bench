#!/usr/bin/env python3
"""Chunked batch runner: a subset of questions per request.

Splits the task list into chunks (default 6) and sends each chunk as one
request over the same document. Answer keys are original task ids, so chunks
can be merged afterwards.

Usage:
  python3 run_batch_chunked.py --dataset dataset_20k.json --model local-only \
      --chunk-size 6 --max-tokens 131072 --out results_next_batch_chunked.json
"""
import argparse
import json
import re
import time
import urllib.error
import urllib.request

BASE = 'http://192.168.1.111:21434'
CLIENT = 'openclaw-batch'

INSTRUCTION = ("\n\nBelow are %d independent questions about this document.\n"
               "Answer with ONE JSON object: key is the question number, value is an integer.\n"
               "No explanations, no markdown. Example: {\"1\": 13, \"2\": -4}\n\n")


def build_prompt(document, tasks):
    qs = "\n".join("%d. %s" % (t["id"], t["question"]) for t in tasks)
    return document + (INSTRUCTION % len(tasks)) + qs + "\n"


def call(prompt, model, max_tokens, timeout=3600):
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(BASE + '/v1/chat/completions', data=body,
                                 headers={'Content-Type': 'application/json', 'X-Aidir-Client': CLIENT})
    t0 = time.time()
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    except urllib.error.HTTPError as e:
        return {"error": "HTTP %s" % e.code, "latency": time.time() - t0}
    except Exception as e:
        return {"error": str(e)[:150], "latency": time.time() - t0}
    ch = (d.get('choices') or [{}])[0]
    msg = ch.get('message') or {}
    return {"content": (msg.get('content') or '').strip(),
            "finish": ch.get('finish_reason'),
            "latency": time.time() - t0, "model": d.get('model'),
            "usage": d.get('usage') or {}}


def parse_answers(text):
    out = {}
    if not text:
        return out
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
    for k, v in re.findall(r"(\d{1,2})\s*[:.)\-—]\s*(-?\d+)", text):
        out.setdefault(int(k), int(v))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--chunk-size", type=int, default=6)
    ap.add_argument("--max-tokens", type=int, default=131072)
    ap.add_argument("--out", default="batch_chunked.json")
    a = ap.parse_args()

    d = json.load(open(a.dataset))
    tasks = d["tasks"]
    chunks = [tasks[i:i + a.chunk_size] for i in range(0, len(tasks), a.chunk_size)]
    print("dataset: %s | model: %s | tasks: %d | chunks: %d | max_tokens: %d"
          % (a.dataset, a.model, len(tasks), len(chunks), a.max_tokens), flush=True)

    rows = []
    for ci, chunk in enumerate(chunks, 1):
        prompt = build_prompt(d["document"], chunk)
        out = call(prompt, a.model, a.max_tokens)
        if out.get("error") and "400" in str(out.get("error")):
            print("  chunk %d: 400, retrying with 65535" % ci, flush=True)
            out = call(prompt, a.model, 65535)
        answers = parse_answers(out.get("content"))
        ok_n = 0
        for t in chunk:
            got = answers.get(t["id"])
            ok = (got == t["answer"])
            ok_n += ok
            rows.append({"id": t["id"], "answer": t["answer"], "got": got, "ok": ok,
                         "chunk": ci, "latency_s": round(out.get("latency", 0), 1),
                         "finish": out.get("finish"), "error": out.get("error")})
        print("  chunk %d: tasks %s | parsed %d/%d | correct %d | %s | %.1f c"
              % (ci, [t["id"] for t in chunk], len(answers), len(chunk), ok_n,
                 out.get("finish"), out.get("latency", 0)), flush=True)

    ok_total = sum(1 for r in rows if r["ok"])
    print("\nTOTAL: %d/%d correct (%.0f%% errors)"
          % (ok_total, len(rows), 100.0 * (len(rows) - ok_total) / len(rows)))
    json.dump({"dataset": a.dataset, "model": a.model, "chunk_size": a.chunk_size,
               "rows": rows}, open(a.out, "w"), ensure_ascii=False, indent=1)
    print("file:", a.out)


if __name__ == "__main__":
    main()
