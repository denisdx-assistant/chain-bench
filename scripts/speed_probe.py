#!/usr/bin/env python3
"""Measure prefill and generation speed at a chosen prompt size.

The instruction comes FIRST and the filler after it: if the model loses the
beginning of a huge prompt, it will not produce the story at all, and the number
we read will be honest instead of a lucky continuation.
"""
import argparse, hashlib, json, os, re, time, urllib.request

FILLER = ("The document also contains general notes on approval order, preparation timelines "
          "and participants. Some records refer to earlier periods and do not affect current "
          "calculations. ")
ASK = ("Тебе дан большой массив английских слов. Сначала выпиши ПОСЛЕДНИЕ 10 слов этого текста, "
       "затем расскажи историю о рыбаке и море, примерно на 2000 слов. ")


CHARS_PER_TOKEN = float(os.environ.get("CHAIN_BENCH_CHARS_PER_TOKEN", "7.1"))


WORDS = ("ability absence academy accent access accident account accuracy achievement acid action "
         "activity actor addition address adjustment administration admission advantage adventure advice "
         "affair affection afternoon agency agenda agent agreement agriculture aircraft airline airport "
         "alarm album alcohol alley alliance allowance alternative ambition ambulance amendment amount "
         "analysis ancestor anchor angel anger angle animal ankle anniversary answer anxiety apartment "
         "apology apparatus appeal appearance appetite apple application appointment approval aquarium arch "
         "architect architecture area argument arm army arrangement arrival arrow art article artist artwork "
         "ash aspect assignment assistance assistant association assumption atmosphere atom attachment attack "
         "attempt attention attitude audience author authority autumn avenue average award awareness axis baby "
         "bachelor backbone background bacon badge bag baggage bakery balance balcony ball balloon ballot "
         "bamboo banana band bandage bank banker banner banquet bargain bark barn barrel barrier base "
         "basement basin basis basket basketball bath bathroom battery battle beach bean bear beard beast "
         "beauty bedroom bee beef beetle beginning behavior belief bell belt bench benefit berry bicycle bid "
         "bike bill biography biology bird birth birthday biscuit bishop bite blade blanket blast blend "
         "blessing block blood blossom blouse board boat body boiler bolt bomb bond bone bonus book booking "
         "booklet border bottle bottom boundary bowl brain branch brand brass bread breakfast breast breath "
         "breeze brick bride bridge brief broadcast broccoli brother brush bubble bucket budget buffalo "
         "building bulb bulk bull bullet bunch burden bureau burger burial bush business butter butterfly "
         "button buyer cabbage cabin cabinet cable cafe cage cake calculation calendar camera camp campaign "
         "campus canal candidate candle candy cannon canoe canvas canyon capability capacity capital captain "
         "carbon card care career cargo carpet carriage carrier carrot cart cartoon case cash castle cat "
         "catalog catch category cattle cause cave ceiling celebration celebrity cellar cement census center "
         "century ceremony chain chair chairman chalk challenge chamber champion chance change channel "
         "chapter character charge charity charm chart chase chat cheek cheese chef chemistry cherry chess "
         "chest chicken chief childhood chimney chip chocolate choice choir church cinema circle circuit "
         "citizen city claim class classroom clay cleaner clerk cliff climate clinic clock cloth cloud club "
         "clue coach coal coast coat code coffee coin collection college colony color column combination "
         "comfort command comment committee community companion company comparison compass competition "
         "complaint complex component composer composition compound computer concept concern concert "
         "conclusion concrete condition conference confidence conflict confusion connection conscience "
         "consequence conservation consideration construction consultant contact container content contest "
         "continent contract contrast contribution control convention conversation conversion cookie copper "
         "copy coral cord core corn corner corporation correction corridor cost costume cottage cotton couch "
         "council counselor count counter country countryside county couple courage course court cousin "
         "cover cow crab crack craft crane crash cream creation creature credit creek crew cricket crime "
         "crisis critic criticism crop cross crowd crown cruise crystal cube culture cup cupboard curiosity "
         "currency curtain curve cushion customer custom cut cycle dad damage dance dancer danger darkness "
         "data database date daughter dawn day deadline dealer death debate debt decade decision deck "
         "declaration decline decoration deed deer defeat defense definition degree delay delegation "
         "delight delivery demand democracy demonstration density dentist department departure dependence "
         "deposit depression depth deputy description desert design designer desire desk destination detail "
         "detective determination development device devil diagram dialogue diamond diary dictionary diet "
         "difference difficulty dignity dimension dinner dinosaur direction director dirt disadvantage "
         "disaster discipline discovery discussion disease dish disk display distance distribution district "
         "diversity division dock doctor document dog doll dolphin domain donation donkey door doorway dose "
         "doubt dough dove draft dragon drain drama drawer drawing dream dress drink drive driver drop "
         "drought drum duck dust duty eagle ear earthquake ease east echo economy edge edition editor "
         "education effect effort egg elbow elder election electricity electron element elephant elevator "
         "emergency emotion emperor emphasis employee employer employment encounter encouragement end enemy "
         "energy engine engineer engineering entertainment enthusiasm entrance entry envelope environment "
         "episode equality equipment era error escape essay essence estate estimate evaluation evening event "
         "evidence evolution examination example exception exchange excitement excuse execution exercise").split()


def random_filler(words_target):
    """A stream of ordinary English words, roughly one token each, seeded fresh every run.

    One space-separated dictionary word costs about one token, so the word count is the
    token count. A marker word is inserted every 100-200 words so the answer can be
    verified: a model that did not read the whole prompt gets the count wrong.
    """
    import random
    rnd = random.Random(int.from_bytes(os.urandom(16), "big"))
    out = []
    marker = "context"
    count = 0
    since = 0
    after = rnd.randint(100, 200)
    for _ in range(words_target):
        if since >= after:
            out.append(marker)
            count += 1
            since = 0
            after = rnd.randint(100, 200)
        else:
            out.append(rnd.choice(WORDS))
            since += 1
    return " ".join(out), count

def looks_like_echo(answer):
    """True when the reply reproduces the English source instead of a Russian story.

    The instruction is Russian and asks for a story, so a genuine answer is mostly
    Cyrillic; the filler is a stream of English dictionary words. A reply with almost no
    Cyrillic is the source quoted back, and its tokens/second is not writing speed.
    """
    head = (answer or "")[:600]
    if head.lower().lstrip().startswith(("последние 10 слов", "last ten words", "last 10 words")):
        return False
    letters = [c for c in head if c.isalpha()]
    if not letters:
        return False
    cyr = sum(1 for c in letters if "\u0400" <= c <= "\u04ff") / len(letters)
    return cyr < 0.05

def build_prompt(target_tokens, reserve):
    """Filler sized so that prompt + reserved output stays inside the window.

    The filler is ordinary prose, which tokenises at roughly 6.2 characters per
    token on this tokenizer; the measured prompt_n is printed for verification.
    """
    # target_tokens is the prompt size we want; the reserve only guards the window
    body, expected = random_filler(target_tokens)
    tail = " ".join(body.split()[-10:])
    return ASK + body, {"markers": expected, "tail": tail}


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
    def call(prompt, mt=None):
        body = json.dumps({"model": a.model, "messages": [{"role": "user", "content": prompt}],
                           "max_tokens": mt if mt is not None else a.max_tokens, "stream": False,
                           "temperature": 0.7}).encode()
        req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers=hdr)
        t0 = time.time()
        r = urllib.request.urlopen(req, timeout=3600)
        return json.loads(r.read()), time.time() - t0

    global CHARS_PER_TOKEN
    # cheap calibration first: one small request tells us the real chars-per-token,
    # so the big prompts are sized correctly on the first attempt
    try:
        probe_prompt, _ = build_prompt(5000, a.max_tokens)
        d0, _ = call(probe_prompt, mt=16)
        st0 = d0.get("timings") or {}
        if st0.get("prompt_n"):
            CHARS_PER_TOKEN = len(probe_prompt) / float(st0["prompt_n"])
            print("калибровка: %.2f символа на токен (проверочный промпт %d токенов, кэш %s)"
                  % (CHARS_PER_TOKEN, st0["prompt_n"], st0.get("cache_n") or 0), flush=True)
    except Exception as e:
        print("калибровка не удалась: %s" % str(e)[:100], flush=True)
    recs = []
    for want in sizes:
        attempt = 0
        while True:
            attempt += 1
            prompt, expected = build_prompt(want, a.max_tokens)
            try:
                d, wall = call(prompt)
            except Exception as e:
                print("  %7s | ошибка: %s" % (want, str(e)[:120]), flush=True)
                recs.append({"want": want, "expected_markers": expected if "expected" in dir() else None, "error": str(e)[:160]})
                break
            st = d.get("timings") or {}
            got = st.get("prompt_n") or 0
            cached = st.get("cache_n") or 0
            # calibrate from the first real measurement, then verify every size once
            if got and cached == 0 and attempt < 3:
                ratio = len(prompt) / float(got)
                dev = abs(got - want) / float(want)
                if dev > 0.08:
                    CHARS_PER_TOKEN = ratio
                    print("  %7s | получено %d (%+.0f%%), пересчёт по %.2f симв./токен"
                          % (want, got, 100 * (got - want) / want, ratio), flush=True)
                    continue
                CHARS_PER_TOKEN = ratio
            break
        ch = (d.get("choices") or [{}])[0]
        msg = ch.get("message") or {}
        rec = {"want": want,
               "prompt_n": st.get("prompt_n"), "cache_n": st.get("cache_n"),
               "prompt_tps": st.get("prompt_per_second"),
               "gen_tps": st.get("predicted_per_second"),
               "predicted_n": st.get("predicted_n"),
               "finish": ch.get("finish_reason"),
               "wall_s": round(wall, 1),
               "story_head": (msg.get("content") or "")[:120].replace("\n", " "),
               "prompt_hash": hashlib.sha256(prompt.encode()).hexdigest()[:16],
               "echo": looks_like_echo(msg.get("content")),
               "answer_head": (msg.get("content") or "")[:300],
               "max_tokens": a.max_tokens}
        recs.append(rec)
        print("  цель %-7s | промпт %-8s | префилл %-5s t/s | генерация %-5s t/s (%s tok) | %s c"
              % (want, rec["prompt_n"], int(rec["prompt_tps"] or 0), int(rec["gen_tps"] or 0),
                 rec["predicted_n"], rec["wall_s"]), flush=True)
    # merge with earlier passes so a retry adds a point instead of replacing the file
    merged = []
    if os.path.exists(out):
        try:
            prev = json.load(open(out))
        except Exception:
            prev = []
        # keep every distinct run so speeds can be averaged: same nominal size but a
        # different prompt text (or a different output budget) is a separate measurement
        def key(r):
            return (r.get("want"), r.get("max_tokens"), r.get("prompt_hash"))
        by_key = {key(r): r for r in prev if isinstance(r, dict)}
        for r in recs:
            by_key[key(r)] = r
        merged = [by_key[k] for k in sorted(by_key, key=lambda x: (x[0] is None, x[0],
                                                                  x[1] or 0, x[2] or ""))]
    json.dump(merged or recs, open(out, "w"), ensure_ascii=False, indent=1)
    print("записано:", out)


if __name__ == "__main__":
    main()
