# Per-task results

Generated from the result files by `scripts/build_task_tables.py`.
Cell format: `seconds mark` — ✓ correct, ✗ wrong, L stopped on the length
cap, R aborted by the loop guard, · task not in this set.

### Summary by test group

Cell format: total wall-clock time of the group and correct/total.

`(8)` marks a run on the 8-task subset instead of the full set.

| Run | Overall | Test 1 en | Test 1 ru | Test 1 zh | Test 2 |
|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default · budget 16k | 28m57s 42% | 5m19s 4/8 (8) | 13m30s 10/17 | 10m08s 5/8 (8) | — |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · budget 16k · guard | 30m22s 38% | 14m42s 11/17 | 15m40s 10/17 | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ctx 262k · no YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 54m01s 90% | — | — | — | 54m01s 2/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 94m29s 65% | — | 30m21s 10/17 | — | 64m08s 3/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T default · budget 65535 | 27m58s 29% | — | 27m58s 12/17 | — | — |

### Test 1 — full 17-task set

| Run | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · default | 23s ✓ | 78s ✗ | 10s ✓ | 8s ✓ | 9s ✓ | 7s ✓ | 73s ✗ | 9s ✓ | 68s ✗ | 51s ✓ | 73s ✓ | 70s ✓ | 62s ✗ | 73s ✗ | 61s ✗ | 74s ✓ | 61s ✗ | 10/17 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 16k · default | 70s ✓ | 78s ✗ | 7s ✓ | 7s ✓ | 7s ✓ | 11s ✓ | 75s ✗ | 13s ✓ | 77s ✗ | 12s ✓ | 79s ✗ | 75s ✗ | 70s ✗ | 76s ✓ | 73s ✓ | 80s ✓ | 72s ✓ | 11/17 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 16k · default | 32s ✓ | 80s ✗ | 9s ✓ | 8s ✓ | 10s ✓ | 8s ✓ | 74s ✗ | 14s ✓ | 75s ✗ | 76s ✓ | 82s ✓ | 76s ✗ | 81s ✗ | 78s ✗ | 80s ✓ | 82s ✓ | 75s ✗ | 10/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ru · 32k · guarded | 157s ✓ | 73s ✗ | 9s ✓ | 8s ✓ | 11s ✓ | 6s ✓ | 131s ✗ | 10s ✓ | 168s ✗ | 27s ✓ | 203s ✓ | 379s L | 202s ✗ | 82s ✗ | 75s ✓ | 97s ✓ | 183s ✗ | 10/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ru · 65535 · default | 62s ✓ | 168s ✗ | 7s ✓ | 6s ✓ | 8s ✓ | 5s ✓ | 250s ✗ | 13s ✓ | 83s ✓ | 20s ✓ | 117s ✓ | 102s ✓ | 320s ✗ | 206s ✗ | 102s ✓ | 53s ✓ | 156s ✗ | 12/17 |

### Test 1 — 8-task subset

| Run | T1 | T2 | T3 | T6 | T7 | T9 | T13 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · en · 16k · 8tasks | 33s ✓ | 6s ✓ | 5s ✓ | 6s ✓ | 70s ✗ | 63s ✗ | 71s ✗ | 65s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · 8tasks | 44s ✓ | 8s ✓ | 6s ✓ | 5s ✓ | 46s ✗ | 46s ✗ | 70s ✗ | 59s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · zh · 16k · 8tasks | 40s ✓ | 11s ✓ | 9s ✓ | 9s ✓ | 37s ✗ | 29s ✗ | 79s ✗ | 394s ✓ | 5/8 |

### Test 2 — 20 frozen programs

| Run | S300 | S301 | S302 | S303 | S304 | S305 | S306 | S307 | S308 | S309 | S310 | S311 | S312 | S313 | S314 | S315 | S316 | S317 | S318 | S319 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · - · 32k · guarded | 305s ✗ | 122s ✗ | 390s ✓ | 132s ✗ | 123s ✗ | 373s ✗ | 124s ✗ | 112s ✗ | 125s ✗ | 111s ✗ | 206s ✗ | 373s ✓ | 120s ✗ | 382s ✓ | 135s ✗ | 146s ✗ | 116s ✗ | 216s ✗ | 126s ✗ | 111s ✗ | 3/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · - · 32k · guarded | 152s ✗ | 388s ✓ | 389s ✓ | 118s ✗ | 192s ✗ | 150s ✗ | 134s ✗ | 114s ✗ | 99s ✗ | 118s ✗ | 120s ✗ | 124s ✗ | 120s ✗ | 132s ✗ | 153s ✗ | 127s ✗ | 133s ✗ | 118s ✗ | 248s ✗ | 112s ✗ | 2/20 |
