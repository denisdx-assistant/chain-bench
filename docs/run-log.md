# Run log

Chronological record of runs and calibration. Times are HKT (UTC+8). Model
names are exact. Scored results live in `results/<model>/`; this page keeps
context and conclusions.

| Date (HKT) | What | Model | Conditions | Result | Conclusion |
|---|---|---|---|---|---|
| 2026-11-03 | Stage 1: 24 tasks | Flash-Next IQ3_S | clean tasks, no noise | 24/24 | basic operations hold |
| 2026-11-03 | Stage 1: 24 tasks | Qwen3.8-27B-UD-Q6_K_XL | clean tasks, no noise | 24/24 | parity in accuracy |
| 2026-11-03 | Stage 2: 60 steps | Flash-Next IQ3_S | context ~20k, cache 99% | 60/60, 0 errors, 1.5 min | no degradation |
| 2026-11-03 | Stage 2: 60 steps | Qwen3.8-27B-UD-Q6_K_XL | context ~20k, cache 99% | 59/60, one 502 | possible glitch, needs retest |
| 2026-11-04 18:10 | Calibration (trial) | Qwen3.8-27B-UD-Q6_K_XL | max_tokens 700 and 3000 | almost all answers empty | budget too small: reasoning consumes it |
| 2026-11-04 18:25 | Calibration: dataset_20k | Qwen3.8-27B-UD-Q6_K_XL | max_tokens 6000 + retry | 6/6 without empties, one quality error (10 vs 6) | 6000 still tight, moved to 16k |
| 2026-11-04 18:37 | Calibration: dataset_20k | Qwen3.8-27B-UD-Q6_K_XL | max_tokens 16000, 126 KB, 300 noise lines | 10/17 (41% errors), no empties | close to the 50% target |
| 2026-11-04 18:49 | Batched run: all 17 in one request | Qwen3.8-27B-UD-Q6_K_XL | 129 KB, max_tokens 16000 | 4/17 (76% errors), 90 s | batching sharply reduces accuracy |
| 2026-11-04 18:52 | Test 2: 8 programs (easy) | Qwen3.8-27B-UD-Q6_K_XL | ops=8, comments=300, extras=100, traps=30 | 8/8 (0% errors) | too easy |
| 2026-11-04 19:10 | Test 2: v1 heavy | Qwen3.8-27B-UD-Q6_K_XL | ops=15, comments=800, extras=300, traps=80 | 7/8 (12% errors) | still easy |
| 2026-11-04 19:10 | Test 2: v2 control flow | Qwen3.8-27B-UD-Q6_K_XL | ops=12, comments=600, extras=200, traps=60 | 7/8 (12% errors) | next level needed |
| 2026-11-04 19:30 | Test 2: v3 nested | Qwen3.8-27B-UD-Q6_K_XL | ops=25, comments=1500, extras=500, traps=120 | 7/8 (12% errors) | still easy |
| 2026-11-04 20:00 | Noise sweep: 2 shapes × 3 levels | Qwen3.8-27B-UD-Q6_K_XL | low/mid/high | 6/6 (0% errors) | noise volume is not the lever |
| 2026-11-04 22:05 | Test 2: v4 × 5 programs | Qwen3.8-27B-UD-Q6_K_XL | ~106k tokens, ops=20, array + sum | 2/5 (60% errors) | target reached and exceeded |
| 2026-11-05 01:10 | Language series: test 1 | Qwen3.8-27B-UD-Q6_K_XL | 8 tasks per language, 3 documents | ru 4/8 (50%), en 4/8 (50%), zh 5/8 (38%) | language effect is small |
| 2026-11-05 01:20 | Test 2: v4 seeds 400–404 | Qwen3.8-27B-UD-Q6_K_XL | ~106k tokens, ops=20 | 5/5 (0% errors) | high variance between batches |
| 2026-11-05 01:36 | Test 2: v4 × 20 programs | Qwen3.8-27B-UD-Q6_K_XL | ~106k tokens, ops=20, seeds 300–319 | 11/20 (45% errors) | stable estimate, frozen for replay |
| 2026-11-05 02:20 | Test 1: full 17, one per request | Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1M | max_tokens 65535, default sampling | 12/17 (29% errors) | comparable to Q6 at large budget |
| 2026-11-05 05:32 | Test 2: v4 × 20 programs | Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1M | guarded, 32k, temp 0.3, freq/pres 0.3 | 3/20 (85% errors), loops 0, length 3 | failures are confident and wrong, not loops |
| 2026-11-05 12:54 | Test 2: v4 × 20 programs | Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | guarded, 32k, temp 0.3, freq/pres 0.3, 262k no YaRN | 2/20 (90% errors), loops 0, length 2 | removing YaRN did not recover accuracy |

## Observations

1. **An empty answer is not a wrong answer.** Counted separately.
2. **Routing changes.** Always record the resolved model id; `local-only` has
   pointed at different weights over time.
3. **Prefix cache** makes repeated questions over one document nearly free and
   inflates apparent speed.
4. **Concurrency limit** on the 27B model is 2; a third request waits and
   inflates measured latency.
5. **One loop was observed** before the guard existed: the model repeated a
   single noise block verbatim until the budget was exhausted. The guard,
   penalties and a moderate cap address it.
6. **A length cut without repetition** is a real under-budget case; it is
   retried at 4× budget and reported separately.
