# Per-task results

Generated from the result files by `scripts/build_task_tables.py`.
Cell format: `seconds mark` — ✓ correct, ✗ wrong, L stopped on the length
cap, R aborted by the loop guard, · task not in this set.

### Test 1 — full 17-task set

| Run | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · default | 23sw ✓ | 78sw ✗ | 10sw ✓ | 8sw ✓ | 9sw ✓ | 7sw ✓ | 73sw ✗ | 9sw ✓ | 68sw ✗ | 51sw ✓ | 73sw ✓ | 70sw ✓ | 62sw ✗ | 73sw ✗ | 61sw ✗ | 74sw ✓ | 61sw ✗ | 10/17 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 16k · default | 70sw ✓ | 78sw ✗ | 7sw ✓ | 7sw ✓ | 7sw ✓ | 11sw ✓ | 75sw ✗ | 13sw ✓ | 77sw ✗ | 12sw ✓ | 79sw ✗ | 75sw ✗ | 70sw ✗ | 76sw ✓ | 73sw ✓ | 80sw ✓ | 72sw ✓ | 11/17 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 16k · default | 32sw ✓ | 80sw ✗ | 9sw ✓ | 8sw ✓ | 10sw ✓ | 8sw ✓ | 74sw ✗ | 14sw ✓ | 75sw ✗ | 76sw ✓ | 82sw ✓ | 76sw ✗ | 81sw ✗ | 78sw ✗ | 80sw ✓ | 82sw ✓ | 75sw ✗ | 10/17 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 16k · default | 115sw ✓ | 83sw ✓ | 10sw ✓ | 9sw ✓ | 11sw ✓ | 10sw ✓ | 83sw ✗ | 40sw ✓ | 84sw ✗ | 68sw ✓ | 87sw ✗ | 86sw ✓ | 83sw ✗ | 87sw ✗ | 88sw ✓ | 49sw ✓ | 83sw ✗ | 11/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ru · 32k · guarded | 157sw ✓ | 73sw ✗ | 9sw ✓ | 8sw ✓ | 11sw ✓ | 6sw ✓ | 131sw ✗ | 10sw ✓ | 168sw ✗ | 27sw ✓ | 203sw ✓ | 379sw L | 202sw ✗ | 82sw ✗ | 75sw ✓ | 97sw ✓ | 183sw ✗ | 10/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ru · 65535 · default | 62sw ✓ | 168sw ✗ | 7sw ✓ | 6sw ✓ | 8sw ✓ | 5sw ✓ | 250sw ✗ | 13sw ✓ | 83sw ✓ | 20sw ✓ | 117sw ✓ | 102sw ✓ | 320sw ✗ | 206sw ✗ | 102sw ✓ | 53sw ✓ | 156sw ✗ | 12/17 |

### Test 1 — 8-task subset

| Run | T1 | T2 | T3 | T6 | T7 | T9 | T13 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · en · 16k · 8tasks | 33sw ✓ | 6sw ✓ | 5sw ✓ | 6sw ✓ | 70sw ✗ | 63sw ✗ | 71sw ✗ | 65sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · 8tasks | 44sw ✓ | 8sw ✓ | 6sw ✓ | 5sw ✓ | 46sw ✗ | 46sw ✗ | 70sw ✗ | 59sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · zh · 16k · 8tasks | 40sw ✓ | 11sw ✓ | 9sw ✓ | 9sw ✓ | 37sw ✗ | 29sw ✗ | 79sw ✗ | 394sw ✓ | 5/8 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 16k · 8tasks | 22sw ✓ | 7sw ✓ | 5sw ✓ | 5sw ✓ | 76sw ✗ | 15sw ✗ | 56sw ✗ | 72sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 16k · 8tasks | 24sw ✓ | 10sw ✓ | 6sw ✓ | 6sw ✓ | 70sw ✗ | 49sw ✗ | 74sw ✗ | 75sw ✓ | 5/8 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 16k · 8tasks | 39sw ✓ | 12sw ✓ | 10sw ✓ | 7sw ✓ | 26sw ✗ | 50sw ✗ | 84sw ✗ | 75sw ✗ | 4/8 |

### Test 2 — 20 frozen programs

| Run | S100 | S101 | S102 | S103 | S104 | S105 | S106 | S107 | S300 | S301 | S302 | S303 | S304 | S305 | S306 | S307 | S308 | S309 | S310 | S311 | S312 | S313 | S314 | S315 | S316 | S317 | S318 | S319 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · - · 8k · legacy | 54sw ✓ | 46sw ✓ | 109sw ✓ | 58sw ✗ | 202sw ✓ | 98sw ✓ | 61sw ✓ | 57sw ✓ | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 7/28 |
| Qwen3.8-27B-UD-Q6_K_XL · - · 8k · legacy | 81sw ✓ | 63sw ✓ | 80sw ✓ | 139sw ✗ | 202sw ✓ | 102sw ✓ | 68sw ✓ | 96sw ✓ | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 7/28 |
| Qwen3.8-27B-UD-Q6_K_XL · - · 16k · default | · | · | · | · | · | · | · | · | 292sw ✓ | 306sw ✗ | 292sw ✗ | 288sw ✗ | 597sw ✓ | 294sw ✓ | 304sw ✓ | 292sw ✓ | 291sw ✓ | 595sw ✓ | 296sw ✗ | 306sw ✗ | 298sw ✗ | 296sw ✗ | 593sw ✓ | 292sw ✓ | 484sw ✗ | 294sw ✓ | 597sw ✗ | 292sw ✓ | 11/28 |
| Qwen3.8-27B-UD-Q8_K_XL · - · 16k · default | · | · | · | · | · | · | · | · | 103s ✓ | 103s ✗ | 105s ✗ | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1/3 (partial 3/20) |
