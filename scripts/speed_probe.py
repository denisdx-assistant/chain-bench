#!/usr/bin/env python3
"""Measure prefill and generation speed at a chosen prompt size.

The instruction comes FIRST and the filler after it: if the model loses the
beginning of a huge prompt, it will not produce the story at all, and the number
we read will be honest instead of a lucky continuation.
"""
import argparse, json, os, re, time, urllib.request

FILLER = ("The document also contains general notes on approval order, preparation timelines "
          "and participants. Some records refer to earlier periods and do not affect current "
          "calculations. ")
ASK = ("Расскажи историю о рыбаке и море, примерно на 2000 слов. Начни сразу с истории. "
       "Затем ниже идёт технический документ, который к истории отношения не имеет.\n\n")


CHARS_PER_TOKEN = float(os.environ.get("CHAIN_BENCH_CHARS_PER_TOKEN", "4.8"))


def unique_filler(chars):
    """Filler whose every sentence carries a distinct number, so the server's prompt
    cache cannot serve it and the measured prefill is the real one."""
    out = []
    n = 0
    size = 0
    while size < chars:
        n += 1
        line = ("Record %d was processed with value %d; general notes on approval order, "
                "preparation timelines and participants follow. Some records refer to "
                "earlier periods and do not affect current calculations. " % (n, n * 7 + 13))
        out.append(line)
        size += len(line)
    return "".join(out)


def build_prompt(target_tokens, reserve):
    """Filler sized so that prompt + reserved output stays inside the window.

    The filler is ordinary prose, which tokenises at roughly 6.2 characters per
    token on this tokenizer; the measured prompt_n is printed for verification.
    """
    body = int(max(0, (target_tokens - reserve) * CHARS_PER_TOKEN))
    return ASK + unique_filler(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--sizes", default="250k,500k,1000k")
    ap.add_argument("--label", default="")
    ap.add_argument("--out-dir", default="results/_speed")
    ap.add_argument("--max-tokens", type=int, default=64000)
    a = ap.parse_args()
    base = os.environ.get("CHAIN_BENCH_ENDPOINT") or open("config/endpoint").read().strip()
    key = os.environ.get("CHAIN_BENCH_API_KEY")
    hdr = {"Content-Type": "application/json",
           "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")}
    if key:
        hdr["Authorization"] = "Bearer " + key
    sizes = []
    for s in a.sizes.split(","):
        s = s.strip().lower()
        mult = {"k": 1000, "m": 1000000}.get(s[-1], 1)
        sizes.append(int(float(s[:-1]) * mult) if s[-1] in "km" else int(s))
    os.makedirs(a.out_dir, exist_ok=True)
    out = os.path.join(a.out_dir, (a.label or a.model).replace("/", "_") + ".json")
    recs = []
    for want in sizes:
        prompt = build_prompt(want, a.max_tokens)
        body = json.dumps({"model": a.model, "messages": [{"role": "user", "content": prompt}],
                           "max_tokens": a.max_tokens, "stream": False,
                           "temperature": 0.7}).encode()
        req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers=hdr)
        t0 = time.time()
        try:
            r = urllib.request.urlopen(req, timeout=3600)
            d = json.loads(r.read())
        except Exception as e:
            print("  %7s | ошибка: %s" % (want, str(e)[:120]), flush=True)
            recs.append({"want": want, "error": str(e)[:160]})
            continue
        st = d.get("timings") or {}
        ch = (d.get("choices") or [{}])[0]
        msg = ch.get("message") or {}
        rec = {"want": want,
               "prompt_n": st.get("prompt_n"), "cache_n": st.get("cache_n"),
               "prompt_tps": st.get("prompt_per_second"),
               "gen_tps": st.get("predicted_per_second"),
               "predicted_n": st.get("predicted_n"),
               "finish": ch.get("finish_reason"),
               "wall_s": round(time.time() - t0, 1),
               "story_head": (msg.get("content") or "")[:120].replace("\n", " ")}
        recs.append(rec)
        print("  цель %-7s | промпт %-8s | префилл %-5s t/s | генерация %-5s t/s (%s tok) | %s c"
              % (want, rec["prompt_n"], int(rec["prompt_tps"] or 0), int(rec["gen_tps"] or 0),
                 rec["predicted_n"], rec["wall_s"]), flush=True)
    json.dump(recs, open(out, "w"), ensure_ascii=False, indent=1)
    print("записано:", out)


if __name__ == "__main__":
    main()
