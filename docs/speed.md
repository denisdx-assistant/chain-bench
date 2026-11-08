# Measured speed per model

Two different things are easy to confuse in the summary table, so they are separated here.

- **Median tokens/task** is how much the model *writes*, not how fast it writes. It is
  the median of `predicted_n` over the tasks of a series. A model that reasons at length
  shows a large number here regardless of its speed.
- **Speed** is measured only from server timings: `prompt_per_second` for prefill and
  `predicted_per_second` for generation. Queue waiting and wall-clock time are excluded.

Series time is roughly `tokens / generation speed`. That is why a model that generates
twice as fast can finish a set in the same time: it also writes noticeably more tokens.
For example, on the English chains the Flash-Next models generate at ~80-98 t/s against
25-60 t/s for the 27B quantisations, but they produce ~5-6k tokens per task against ~4k,
and the 27B host serves the repeated 14k prompt from cache, so its prefill costs almost
nothing.

Prefill numbers come only from requests with an empty prompt cache: a cached request
reports the speed of the few uncached tokens, which is not comparable. Generation does not
depend on the cache, so every run of the right size counts there.

## Table

| Model | Prefill 5k | Prefill 20k | Prefill 60k | Prefill 150k | Prefill 250k | Prefill 500k | Prefill 1M | Gen 5k | Gen 20k | Gen 60k | Gen 150k | Gen 250k | Gen 500k | Gen 1M | Tokens/task | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M | — | 922 t/s | 862 t/s | 433 t/s | — | — | — | — | 23 t/s | 23 t/s | 26 t/s | — | — | — | 4144 | host A, single GPU |
| Qwen3.8-27B-UD-Q6_K_XL | — | 1557 t/s | 1342 t/s | — | — | — | — | — | 62 t/s | 54 t/s | — | — | — | — | 4099 | host A |
| Qwen3.8-27B-UD-Q8_K_XL | — | 1327 t/s | — | 721 t/s | — | — | — | — | 58 t/s | 53 t/s | 40 t/s | — | — | — | 4100 | host A |
| Qwen3.8-Flash-Next-Abiray-Coder-IQ1_M | — | 1899 t/s | 2412 t/s | 2723 t/s | — | — | — | — | 85 t/s | 81 t/s | 86 t/s | — | — | — | 8743 | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | — | 1496 t/s | 2085 t/s | 2438 t/s | — | — | — | — | 90 t/s | 89 t/s | 98 t/s | — | — | — | 4899 | host A |
| Qwen3.8-Flash-Next-UD-IQ4_XS | — | 1480 t/s | 2029 t/s | 2389 t/s | 2427 t/s | 2278 t/s | 2058 t/s | — | 86 t/s | 88 t/s | 96 t/s | 119 t/s | 111 t/s | 50 t/s | 5511 | host A (2xV100) |
| Qwen3.8-Flash-Next-UD-Q4_K_XL | — | 1132 t/s | 1530 t/s | 1796 t/s | — | — | — | — | 78 t/s | 79 t/s | 83 t/s | — | — | — | 5211 | host A (2xV100) |
| Ripple-65B-Preview-Q6_K | — | 482 t/s | — | 372 t/s | — | — | — | — | 20 t/s | — | 14 t/s | — | — | — | 10428 | host A (2xV100) |
| gemma-4-31B-it-UD-Q8_K_XL | — | 1041 t/s | — | 494 t/s | — | — | — | — | 71 t/s | 60 t/s | 43 t/s | — | — | — | 1601 | host A (2xV100) |

## What the 250k/500k/1M columns measure

Columns 250k, 500k and 1M are **not** measured on the benchmark tasks. They come from a
separate synthetic probe (`scripts/speed_probe.py`):

- the prompt is a stream of ordinary English words, about one token per word, drawn from
  `os.urandom` fresh for every run, so the server's prompt cache cannot serve it;
- the instruction comes first and asks for the last ten words of the text, then for a
  story. Repeating the tail proves the model reached the end of the prompt; it costs a
  couple of lines and does not invite an echo of the whole document;
- the sizes are calibrated on a 5k-token request before the big ones, so `prompt_n` lands
  within about half a percent of the target;
- a point is accepted only with `cache_n = 0` and an actual prompt within 5% of the target;
- the 1M column is probed at 900k: a full 1M prompt leaves no room for an answer inside
  the 1 000 000-token window, so 900k plus a 64k budget is the largest honest point;

**Read them as an upper bound, not as a task expectation.** Generation there is uniform
prose, which is the friendliest case for draft/MTP decoding; on real tasks the model
produces long structured reasoning and code, and the effective speed is lower. The 60k
and 150k columns, by contrast, are measured on the actual test sets.

## Averaging the probe runs

Every distinct run at a size is kept, not just the last one: a retry with a different output
budget or a different prompt text is a separate measurement, keyed by target size, budget
and prompt hash. Repeated passes at one size are averaged, so a long run is never wasted.

The earlier deterministic-filler runs do not qualify: they hit the cache, and they also
missed their target size — 181k, 425k and 815k tokens of prompt against 250k, 500k and 1M —
because the character-per-token ratio was guessed rather than measured.

## The earlier probe was deterministic, and the cache proved it

The first attempt at these sizes tried to defeat the cache with filler whose every sentence
carried a different number. That filler was **fully deterministic**: the same size produced
byte-identical text on every run. So the second request at a given size was a prefix match
of the first, and the server rightly served it from cache — `cache_n` of 114 688, 262 144
and 409 600 tokens against `prompt_n` of 66 789, 163 157 and 405 825.

A cache hit on a supposedly unique prompt is a bug report, not a server artefact: it means
the generated text repeated.

## Findings from the large probes (IQ4_XS, 2xV100)

| Target | Prompt | Cache | Prefill | Gen | Written | Finish | What it did |
|---|---|---|---|---|---|---|---|
| 250k | 251 219 | 0 | 2401 t/s | 154 t/s | 64 000 | length | re-quoted the source text |
| 250k retry | 251 219 | 0 | 2454 t/s | 84 t/s | 23 822 | stop | quoted the last ten words, then wrote the story |
| 500k | 502 354 | 0 | 2278 t/s | 111 t/s | 61 383 | stop | answered, then wrote the story |
| 900k | 904 358 | 0 | 2058 t/s | 50 t/s | 4 394 | stop | discussed the count, no story |

On the 250k prompt the model did not loop and did not cut early: it spent the whole output
budget re-quoting the source. No context window would have been enough for that variant of
the task — the request failed, not the budget. That is why the check changed to the last ten
words.

The 154 t/s on that point is an echo-driven upper bound, not a generation speed. Repeating
the same size with the tail check and a 128k budget gave 84 t/s: the model printed the last
ten words, then wrote the story and stopped by itself. That is the number to trust, and both
runs stay in the file so the column shows their average.

The 900k point is the opposite case: prefill is a real 2058 t/s, but the answer stopped
after 4 394 tokens without a story, so its generation figure is not comparable either.

## Gaps

The 5k bucket has no rows yet: every series used prompts of ~14k (chains) or ~142k
(programs). The 250k/500k/1M columns are filled for IQ4_XS only; the other models need the
same probe while they are loaded.

## Regenerating

```
python3 scripts/build_speed_table.py
python3 scripts/update_speed_doc.py
```

## Continuous batching

Flash-Next providers serve with continuous batching, so a new request's prompt processing
can be interleaved with the decode steps of requests already in flight. When that happens
the server's own `prompt_ms` and `predicted_ms` overlap instead of following each other:
their sum exceeds the wall time, and neither number describes a clean measurement.

The rule that follows is simple: **measure with one client, one request at a time.** These
series do exactly that, and the additivity is checked rather than assumed — `wall / (prompt_ms
+ predicted_ms)` sits at 1.00-1.02 for every row of every run in this repository, which is
request overhead and nothing more.

`scripts/check_overlap.py` scans the results and reports any row where the sum exceeds the
wall time, i.e. where prefill and generation really did overlap. Such rows must be kept out
of speed tables: on a batched server the reported `prompt_per_second` is not the speed of
reading the prompt, it is the speed of reading it while something else was being written.

## What batching actually cost (IQ1_M, two clients)

The Chinese chains were run twice: once as one stream, once with two requests kept in
flight, which is the provider's configured limit. Same tasks, same 64k budget.

| Mode | Correct | Gen per stream | Aggregate | Wall | Tokens |
|---|---|---|---|---|---|
| one client | 11/17 | 83.2 t/s | 78.3 tok/s | 2 224 s | 174 172 |
| two clients | 11/17 | 59.2 t/s | 72.3 tok/s | 2 407 s | 173 977 |

Every row of the two-client run overlapped another request (`concurrent_peers` > 0), so the
batching was real and not just queued.

**Batching made it slower on both counts.** Each stream dropped 29%, from 83 to 59 t/s, and
aggregate throughput fell too, from 78 to 72 tok/s, while the series took 8% longer. One
stream already saturates memory bandwidth on this GPU pair, so a second stream only adds
switching cost. For this model, one client per GPU is the faster arrangement.
