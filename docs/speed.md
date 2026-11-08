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

Prefill numbers below come only from requests with an empty prompt cache: a cached
request reports the speed of the few uncached tokens, which is not comparable.

## Table

| Model | Prefill 5k | Prefill 20k | Prefill 60k | Prefill 150k | Prefill 250k | Prefill 500k | Prefill 1M | Gen 5k | Gen 20k | Gen 60k | Gen 150k | Gen 250k | Gen 500k | Gen 1M | Tokens/task | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M | — | 922 t/s | 862 t/s | 433 t/s | — | — | — | — | 23 t/s | 23 t/s | 26 t/s | — | — | — | 4144 | host A, single GPU |
| Qwen3.8-27B-UD-Q6_K_XL | — | 1557 t/s | 1342 t/s | — | — | — | — | — | 62 t/s | 54 t/s | — | — | — | — | 4099 | host A |
| Qwen3.8-27B-UD-Q8_K_XL | — | 1327 t/s | — | 721 t/s | — | — | — | — | 58 t/s | 53 t/s | 40 t/s | — | — | — | 4100 | host A |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | — | 1496 t/s | 2085 t/s | 2438 t/s | — | — | — | — | 90 t/s | 89 t/s | 98 t/s | — | — | — | 4899 | host A |
| Qwen3.8-Flash-Next-UD-IQ4_XS | — | 1480 t/s | 2029 t/s | 2389 t/s | — | — | — | — | 86 t/s | 88 t/s | 96 t/s | — | — | — | 5511 | host A (2xV100) |
| Qwen3.8-Flash-Next-UD-Q4_K_XL | — | 1132 t/s | 1530 t/s | 1796 t/s | — | — | — | — | 78 t/s | 79 t/s | 83 t/s | — | — | — | 5211 | host A (2xV100) |
| Ripple-65B-Preview-Q6_K | — | 482 t/s | — | 372 t/s | — | — | — | — | 20 t/s | — | 14 t/s | — | — | — | 10428 | host A (2xV100) |
| gemma-4-31B-it-UD-Q8_K_XL | — | 1041 t/s | — | 494 t/s | — | — | — | — | 71 t/s | 60 t/s | 43 t/s | — | — | — | 1601 | host A (2xV100) |
