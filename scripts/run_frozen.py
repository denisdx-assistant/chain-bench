#!/usr/bin/env python3
"""Replay frozen programs: identical inputs for every model.

Reads a directory of `*.py` with matching `*.json` (expected array and sum),
asks the model for the final array and sum, and compares element-wise.

Usage:
  python3 run_frozen.py --dir datasets/programs/v4 --model local-only --out results/replay.json
"""
import argparse
import glob
import json
import os
import re
import time
import urllib.error
import urllib.request

BASE = 'http://192.168.1.111:21434'
CLIENT = 'openclaw-frozen'
QUESTION = ("\n\nQuestion: name the final array arr after running this program and its sum. "
            "Answer strictly as:\nARRAY: [numbers, comma separated]\nSUM: number")


def ask(code, model, max_tokens=16000, timeout=3600):
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": code + QUESTION}]}).encode()
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
            "reasoning_chars": len(msg.get('reasoning_content') or ''),
            "finish": ch.get('finish_reason'),
            "latency": time.time() - t0, "model": d.get('model')}


def parse_array(text):
    m = re.search(r'ARRAY:\s*\[([^\]]*)\]', text or '')
    if not m:
        return None
    nums = [int(x) for x in re.findall(r'-?\d+', m.group(1))]
    return nums if len(nums) == 10 else None


def parse_sum(text):
    m = re.search(r'SUM:\s*(-?\d+)', text or '')
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--model", default="local-only")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--out", default="replay.json")
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.dir, "*.py")))
    if a.limit:
        files = files[:a.limit]
    print("dir: %s | model: %s | programs: %d" % (a.dir, a.model, len(files)), flush=True)

    rows = []
    for path in files:
        meta_path = path[:-3] + ".json"
        meta = json.load(open(meta_path))
        code = open(path).read()
        out = ask(code, a.model, a.max_tokens)
        got_arr = parse_array(out.get('content'))
        got_sum = parse_sum(out.get('content'))
        exp_arr = json.loads(meta["expected_array"]) if isinstance(meta["expected_array"], str) else meta["expected_array"]
        ok = (got_arr == exp_arr and got_sum == meta["expected_sum"])
        rows.append({"file": os.path.basename(path), "seed": meta.get("seed"),
                     "expected_sum": meta["expected_sum"], "got_sum": got_sum,
                     "expected_array": exp_arr, "got_array": got_arr, "ok": ok,
                     "latency_s": round(out.get('latency', 0), 1),
                     "finish": out.get('finish'), "error": out.get('error'),
                     "raw": (out.get('content') or '')[:200]})
        print("  %-22s | expected %5s | got %5s | %s | %5.1f c"
              % (os.path.basename(path), meta["expected_sum"], got_sum,
                 "OK" if ok else "FAIL", out.get('latency', 0)), flush=True)

    ok_n = sum(1 for r in rows if r['ok'])
    print("\nTOTAL: %d/%d correct (%.0f%% errors)" % (ok_n, len(rows), 100.0 * (len(rows) - ok_n) / max(1, len(rows))))
    json.dump({"model": a.model, "dir": a.dir, "rows": rows}, open(a.out, 'w'), ensure_ascii=False, indent=1)
    print("file:", a.out)


if __name__ == '__main__':
    main()
