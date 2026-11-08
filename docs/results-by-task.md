# Per-task results

Generated from the result files by `scripts/build_task_tables.py`.
Cell format: `seconds mark` — ✓ correct, ✗ wrong, L stopped on the length
cap, R aborted by the loop guard, · task not in this set.

### Test 1 — full 17-task set

| Run | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M · en · 16k · default | 112s ✓ | 659s ✓ | 14s ✓ | 14s ✓ | 19s ✓ | 17s ✓ | 874s ✓ | 30s ✓ | 421s ✗ | 224s ✓ | 549s ✗ | 800s ✗ | 703s ✗ | 700s ✗ | 534s ✓ | 147s ✓ | 684s ✓ | 12/17 |
| Qwen3.8-27B-UD-Q4_K_M · ru · 16k · default | 174sw ✓ | 617sw ✗ | 12sw ✓ | 21sw ✓ | 18sw ✓ | 11sw ✓ | 396sw ✗ | 62sw ✓ | 561sw ✗ | 106sw ✓ | 447sw ✓ | 673s ✓ | 724s ✗ | 714s ✗ | 163s ✓ | 173s ✓ | 724s ✗ | 11/17 |
| Qwen3.8-27B-UD-Q4_K_M · zh · 16k · default | 217s ✓ | 351s ✓ | 18s ✓ | 13s ✓ | 13s ✓ | 24s ✓ | 670s ✓ | 80s ✓ | 570s ✗ | 113s ✓ | 505s ✗ | 778s ✗ | 622s ✗ | 908s ✓ | 224s ✓ | 125s ✓ | 277s ✗ | 12/17 |
| Qwen3.8-27B-UD-Q6_K_XL · en · 16k · default | 65s ✓ | 70s ✓ | 6s ✓ | 6s ✓ | 7s ✓ | 5s ✓ | 70s ✓ | 10s ✓ | 67s ✗ | 64s ✓ | 70s ✗ | 66s ✓ | 69s ✗ | 66s ✓ | 68s ✓ | 72s ✓ | 65s ✗ | 13/17 |
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · default | 23sw ✓ | 78sw ✗ | 10sw ✓ | 8sw ✓ | 9sw ✓ | 7sw ✓ | 73sw ✗ | 9sw ✓ | 68sw ✗ | 51sw ✓ | 73sw ✓ | 70sw ✓ | 62sw ✗ | 73sw ✗ | 61sw ✗ | 74sw ✓ | 61sw ✗ | 10/17 |
| Qwen3.8-27B-UD-Q6_K_XL · zh · 16k · default | 103s ✓ | 82s ✓ | 7s ✓ | 8s ✓ | 8s ✓ | 7s ✓ | 75s ✓ | 31s ✓ | 77s ✗ | 52s ✓ | 81s ✗ | 75s ✗ | 78s ✓ | 78s ✓ | 84s ✗ | 80s ✓ | 78s ✗ | 12/17 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 16k · default | 70sw ✓ | 78sw ✗ | 7sw ✓ | 7sw ✓ | 7sw ✓ | 11sw ✓ | 75sw ✗ | 13sw ✓ | 77sw ✗ | 12sw ✓ | 79sw ✗ | 75sw ✗ | 70sw ✗ | 76sw ✓ | 73sw ✓ | 80sw ✓ | 72sw ✓ | 11/17 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 32k · rerun | 27s ✓ | 69s ✓ | 4s ✓ | 6s ✓ | 8s ✓ | 9s ✓ | 76s ✗ | 10s ✓ | 75s ✗ | 25s ✓ | 75s ✗ | 73s ✗ | 72s ✗ | 74s ✓ | 74s ✓ | 76s ✓ | 72s ✗ | 11/17 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 16k · default | 32sw ✓ | 80sw ✗ | 9sw ✓ | 8sw ✓ | 10sw ✓ | 8sw ✓ | 74sw ✗ | 14sw ✓ | 75sw ✗ | 76sw ✓ | 82sw ✓ | 76sw ✗ | 81sw ✗ | 78sw ✗ | 80sw ✓ | 82sw ✓ | 75sw ✗ | 10/17 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 32k · rerun | 59s ✓ | 76s ✗ | 8s ✓ | 8s ✓ | 7s ✓ | 6s ✓ | 75s ✗ | 14s ✓ | 73s ✗ | 9s ✓ | 73s ✓ | 72s ✗ | 75s ✗ | 74s ✗ | 74s ✓ | 59s ✓ | 68s ✗ | 10/17 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 16k · default | 115sw ✓ | 83sw ✓ | 10sw ✓ | 9sw ✓ | 11sw ✓ | 10sw ✓ | 83sw ✗ | 40sw ✓ | 84sw ✗ | 68sw ✓ | 87sw ✗ | 86sw ✓ | 83sw ✗ | 87sw ✗ | 88sw ✓ | 49sw ✓ | 83sw ✗ | 11/17 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 32k · rerun | 112s ✓ | 84s ✓ | 9s ✓ | 8s ✓ | 8s ✓ | 8s ✓ | 84s ✗ | 45s ✓ | 79s ✗ | 48s ✓ | 83s ✗ | 81s ✓ | 82s ✗ | 79s ✓ | 78s ✓ | 86s ✓ | 76s ✗ | 12/17 |
| Qwen3.8-Flash-Next-Abiray-Coder-IQ1_M · en · 64k · default | 25s ✓ | 104s ✓ | 11s ✓ | 12s ✓ | 10s ✓ | 14s ✓ | · | · | · | · | · | · | · | · | · | · | · | 6/6 (partial 6/17) |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · en · 32k · guarded | 43s ✓ | 112s ✓ | 12s ✓ | 12s ✓ | 13s ✓ | 13s ✓ | 125s ✓ | 16s ✓ | 97s ✗ | 30s ✓ | 88s ✗ | 283s ✗ | 121s ✗ | 98s ✓ | 45s ✓ | 66s ✓ | 317s ✗ | 12/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ru · 32k · guarded | 157sw ✓ | 73sw ✗ | 9sw ✓ | 8sw ✓ | 11sw ✓ | 6sw ✓ | 131sw ✗ | 10sw ✓ | 168sw ✗ | 27sw ✓ | 203sw ✓ | 214sw ✓ | 202sw ✗ | 82sw ✗ | 75sw ✓ | 97sw ✓ | 183sw ✗ | 11/17 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · zh · 32k · guarded | 30s ✓ | 72s ✓ | 11s ✓ | 8s ✓ | 10s ✓ | 10s ✓ | 300s ✗ | 16s ✓ | 70s ✗ | 24s ✓ | 62s ✗ | 185s ✗ | 299s ✗ | 128s ✓ | 146s ✓ | 120s ✓ | 379s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · en · 16k · default | 67s ✓ | 89s ✓ | 13s ✓ | 13s ✓ | 12s ✓ | 13s ✓ | 228s ✓ | 15s ✓ | 94s ✗ | 18s ✓ | 133s ✗ | 199s ✗ | 194s ✗ | 183s ✓ | 26s ✓ | 50s ✓ | 251s ✗ | 12/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · en · 64k · rerun | 60s ✓ | 95s ✗ | 13s ✓ | 13s ✓ | 12s ✓ | 12s ✓ | 167s ✓ | 15s ✓ | 79s ✗ | 14s ✓ | 337s ✗ | 389s ✗ | 275s ✗ | 327s ✓ | 85s ✓ | 92s ✓ | 177s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ru · 16k · default | 34s ✓ | 85s ✗ | 9s ✓ | 8s ✓ | 7s ✓ | 6s ✓ | 170s ✗ | 13s ✓ | 150s ✗ | 39s ✓ | 102s ✓ | 234s ✓ | 262s ✗ | 163s ✗ | 90s ✓ | 106s ✓ | 106s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ru · 64k · rerun | 30s ✓ | 107s ✗ | 8s ✓ | 7s ✓ | 7s ✓ | 7s ✓ | 158s ✗ | 29s ✓ | 102s ✗ | 22s ✓ | 164s ✓ | 351s ✓ | 179s ✗ | 261s ✗ | 69s ✓ | 68s ✓ | 131s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · zh · 16k · default | 45s ✓ | 91s ✓ | 19s ✓ | 24s ✓ | 19s ✓ | 17s ✓ | 239s ✓ | 29s ✓ | 82s ✓ | 37s ✓ | 80s ✗ | 133s ✗ | 171s ✗ | 144s ✓ | 117s ✓ | 141s ✓ | 229s ✗ | 13/17 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · zh · 64k · rerun | 54s ✓ | 33s ✗ | 10s ✓ | 9s ✓ | 10s ✓ | 11s ✓ | 116s ✗ | 19s ✓ | 94s ✗ | 12s ✓ | 19s ✓ | 71s ✓ | 273s ✗ | 116s ✓ | 42s ✓ | 140s ✓ | 338s ✗ | 12/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · en · 16k · default | 44s ✓ | 195s ✓ | 16s ✓ | 15s ✓ | 16s ✓ | 16s ✓ | 153s ✓ | 17s ✓ | 119s ✗ | 35s ✓ | 99s ✗ | 328s ✗ | 242s ✗ | 168s ✓ | 67s ✓ | 40s ✓ | 401s ✓ | 13/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · en · 32k · rerun | 42s ✓ | 151s ✓ | 16s ✓ | 16s ✓ | 17s ✓ | 16s ✓ | 122s ✓ | 17s ✓ | 106s ✗ | 26s ✓ | 76s ✗ | 412s L | 269s ✗ | 313s ✓ | 114s ✓ | 86s ✓ | 347s ✗ | 12/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ru · 16k · default | 65s ✓ | 124s ✗ | 21s ✓ | 11s ✓ | 13s ✓ | 10s ✓ | 134s ✗ | 23s ✓ | 145s ✗ | 24s ✓ | 127s ✓ | 297s ✓ | 210s ✗ | 248s ✗ | 71s ✓ | 55s ✓ | 195s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ru · 32k · rerun | 38s ✓ | 159s ✗ | 11s ✓ | 11s ✓ | 13s ✓ | 11s ✓ | 144s ✗ | 27s ✓ | 134s ✗ | 20s ✓ | 92s ✓ | 358s ✓ | 188s ✗ | 162s ✗ | 87s ✓ | 69s ✓ | 105s ✗ | 11/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · zh · 16k · default | 73s ✓ | 149s ✓ | 22s ✓ | 22s ✓ | 24s ✓ | 23s ✓ | 263s ✓ | 56s ✓ | 84s ✓ | 66s ✓ | 127s ✗ | 284s ✓ | 246s ✗ | 176s ✓ | 82s ✓ | 86s ✓ | 344s ✗ | 14/17 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · zh · 32k · rerun | 196s ✗ | 157s ✓ | 14s ✓ | 13s ✓ | 13s ✓ | 13s ✓ | 128s ✓ | 58s ✓ | 90s ✓ | 64s ✓ | 205s ✗ | 150s ✓ | 224s ✗ | 180s ✓ | 64s ✓ | 59s ✓ | 287s ✗ | 13/17 |
| Ripple-65B-Preview-Q6_K · en · 16k · default | 174s ✓ | 514s ✓ | 8s ✓ | 14s ✓ | 11s ✓ | 11s ✓ | 1180s ✓ | 18s ✓ | 247s ✗ | 38s ✓ | 370s ✗ | 1692s L | 1017s ✗ | 586s ✓ | 215s ✓ | 757s ✓ | 405sw R | 12/17 |
| deepseek-v4.1-flash · en · 16k · default | 4sw ✓ | 36sw ✗ | 1sw ✓ | 1sw ✓ | 2sw ✓ | 1sw ✓ | 72sw ✓ | 2sw ✓ | 16sw ✗ | 3sw ✓ | 50sw ✗ | 57sw ✗ | 48sw ✗ | 67sw ✓ | 5sw ✓ | 12sw ✓ | 47sw ✓ | 12/17 |
| gemma-4-31B-it-UD-Q8_K_XL · en · 16k · default | 17s ✓ | 25s ✓ | 5s ✓ | 7s ✓ | 6s ✓ | 6s ✓ | 115s ✗ | 7s ✓ | 97s ✗ | 7s ✓ | 33s ✗ | 131s ✗ | 80s ✗ | 86s ✗ | 15s ✓ | 20s ✗ | 43s ✗ | 9/17 |
| gemma-4-31B-it-UD-Q8_K_XL · ru · 16k · default | 26s ✓ | 16s ✗ | 6s ✓ | 6s ✓ | 7s ✓ | 8s ✓ | 39s ✗ | 7s ✓ | 19s ✗ | 6s ✓ | 38s ✗ | 113s ✓ | 42s ✗ | 32s ✗ | 15s ✓ | 33s ✓ | 31s ✗ | 10/17 |
| gemma-4-31B-it-UD-Q8_K_XL · zh · 16k · default | 6s ✓ | 18s ✓ | 7s ✓ | 8s ✓ | 9s ✓ | 7s ✓ | 58s ✓ | 9s ✓ | 26s ✗ | 9s ✓ | 34s ✗ | 56s ✗ | 45s ✗ | 46s ✓ | 19s ✗ | 19s ✓ | 126s ✗ | 11/17 |

### Test 1 — 8-task subset

| Run | T1 | T2 | T3 | T6 | T7 | T9 | T13 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M · en · 16k · 8tasks | 34s ✓ | 12s ✓ | 11s ✓ | 15s ✓ | 96s ✗ | 29s ✗ | 41s ✗ | 87s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q4_K_M · ru · 16k · 8tasks | 43s ✓ | 19s ✓ | 11s ✓ | 12s ✓ | 88s ✗ | 94s ✗ | 92s ✗ | 87s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q4_K_M · zh · 16k · 8tasks | 88s ✓ | 16s ✓ | 14s ✓ | 13s ✓ | 109s ✗ | 105s ✗ | 110s ✗ | 108s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · en · 16k · 8tasks | 33sw ✓ | 6sw ✓ | 5sw ✓ | 6sw ✓ | 70sw ✗ | 63sw ✗ | 71sw ✗ | 65sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · 8tasks | 44sw ✓ | 8sw ✓ | 6sw ✓ | 5sw ✓ | 46sw ✗ | 46sw ✗ | 70sw ✗ | 59sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q6_K_XL · zh · 16k · 8tasks | 40sw ✓ | 11sw ✓ | 9sw ✓ | 9sw ✓ | 37sw ✗ | 29sw ✗ | 79sw ✗ | 394sw ✓ | 5/8 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 16k · 8tasks | 22sw ✓ | 7sw ✓ | 5sw ✓ | 5sw ✓ | 76sw ✗ | 15sw ✗ | 56sw ✗ | 72sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q8_K_XL · en · 32k · rerun_8tasks | 40s ✓ | 10s ✓ | 6s ✓ | 6s ✓ | 77s ✗ | 20s ✗ | 75s ✗ | 71s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 16k · 8tasks | 24sw ✓ | 10sw ✓ | 6sw ✓ | 6sw ✓ | 70sw ✗ | 49sw ✗ | 74sw ✗ | 75sw ✓ | 5/8 |
| Qwen3.8-27B-UD-Q8_K_XL · ru · 32k · rerun_8tasks | 37s ✓ | 8s ✓ | 7s ✓ | 8s ✓ | 74s ✗ | 42s ✗ | 73s ✗ | 63s ✗ | 4/8 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 16k · 8tasks | 39sw ✓ | 12sw ✓ | 10sw ✓ | 7sw ✓ | 26sw ✗ | 50sw ✗ | 84sw ✗ | 75sw ✗ | 4/8 |
| Qwen3.8-27B-UD-Q8_K_XL · zh · 32k · rerun_8tasks | 67s ✓ | 10s ✓ | 8s ✓ | 8s ✓ | 43s ✗ | 30s ✗ | 83s ✗ | 79s ✓ | 5/8 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · en · 32k · guarded_8tasks | 21s ✓ | 12s ✓ | 11s ✓ | 12s ✓ | 30s ✗ | 19s ✓ | 45s ✗ | 71s ✗ | 5/8 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ru · 32k · guarded_8tasks | 26s ✓ | 10s ✓ | 7s ✓ | 8s ✓ | 41s ✗ | 52s ✗ | 47s ✗ | 109s ✓ | 5/8 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · zh · 32k · guarded_8tasks | 31s ✓ | 13s ✓ | 9s ✓ | 8s ✓ | 56s ✗ | 35s ✗ | 43s ✗ | 79s ✓ | 5/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · en · 16k · 8tasks | 57s ✓ | 12s ✓ | 13s ✓ | 12s ✓ | 28s ✗ | 22s ✓ | 71s ✗ | 233s ✗ | 5/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · en · 64k · rerun_8tasks | 19s ✓ | 14s ✓ | 13s ✓ | 12s ✓ | 68s ✗ | 23s ✗ | 29s ✗ | 231s ✗ | 4/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ru · 16k · 8tasks | 26s ✓ | 12s ✓ | 7s ✓ | 6s ✓ | 39s ✗ | 40s ✗ | 52s ✗ | 156s ✓ | 5/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ru · 64k · rerun_8tasks | 22s ✓ | 10s ✓ | 7s ✓ | 7s ✓ | 42s ✗ | 36s ✓ | 62s ✗ | 52s ✓ | 6/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · zh · 16k · 8tasks | 26s ✓ | 19s ✓ | 17s ✓ | 16s ✓ | 41s ✗ | 47s ✗ | 93s ✗ | 124s ✓ | 5/8 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · zh · 64k · rerun_8tasks | 26s ✓ | 12s ✓ | 9s ✓ | 9s ✓ | 46s ✗ | 38s ✓ | 56s ✗ | 190s ✓ | 6/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · en · 16k · 8tasks | 19s ✓ | 16s ✓ | 15s ✓ | 16s ✓ | 87s ✗ | 28s ✗ | 76s ✗ | 294s ✗ | 4/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · en · 32k · rerun_8tasks | 23s ✓ | 16s ✓ | 16s ✓ | 17s ✓ | 129s ✗ | 31s ✓ | 51s ✗ | 339s ✗ | 5/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ru · 16k · 8tasks | 23s ✓ | 14s ✓ | 12s ✓ | 10s ✓ | 89s ✗ | 62s ✗ | 52s ✗ | 147s ✓ | 5/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ru · 32k · rerun_8tasks | 30s ✓ | 15s ✓ | 11s ✓ | 11s ✓ | 83s ✗ | 47s ✗ | 118s ✗ | 127s ✓ | 5/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · zh · 16k · 8tasks | 43s ✓ | 34s ✓ | 23s ✓ | 22s ✓ | 86s ✗ | 45s ✓ | 83s ✗ | 256s ✓ | 6/8 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · zh · 32k · rerun_8tasks | 32s ✓ | 14s ✓ | 13s ✓ | 12s ✓ | 75s ✗ | 51s ✓ | 28s ✗ | 96s ✓ | 6/8 |
| gemma-4-31B-it-UD-Q8_K_XL · en · 16k · 8tasks | 18s ✓ | 5s ✓ | 6s ✓ | 7s ✓ | 76s ✗ | 7s ✗ | 41s ✗ | 131s ✗ | 4/8 |
| gemma-4-31B-it-UD-Q8_K_XL · ru · 16k · 8tasks | 24s ✓ | 7s ✓ | 6s ✓ | 7s ✓ | 22s ✗ | 12s ✗ | 29s ✗ | 50s ✓ | 5/8 |
| gemma-4-31B-it-UD-Q8_K_XL · zh · 16k · 8tasks | 55s ✓ | 10s ✓ | 6s ✓ | 6s ✓ | 35s ✗ | 15s ✗ | 26s ✗ | 76s ✓ | 5/8 |

### Test 2 — 20 frozen programs

| Run | S300 | S301 | S302 | S303 | S304 | S305 | S306 | S307 | S308 | S309 | S310 | S311 | S312 | S313 | S314 | S315 | S316 | S317 | S318 | S319 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M · - · 16k · default | 489s ✓ | 488s ✗ | 490s ✗ | 489s ✓ | 489s ✓ | 485s ✓ | 295s ✗ | 491s ✓ | 487s ✗ | 490s ✓ | 493s ✓ | 488s ✓ | 159s ✓ | 160s ✓ | 494s ✓ | 487s ✓ | 159s ✓ | 492s ✓ | 494s ✓ | 810s ✗ | 15/20 |
| Qwen3.8-27B-UD-Q6_K_XL · - · 16k · default | 292sw ✓ | 306sw ✗ | 292sw ✗ | 288sw ✗ | 597sw ✓ | 294sw ✓ | 304sw ✓ | 292sw ✓ | 291sw ✓ | 595sw ✓ | 296sw ✗ | 306sw ✗ | 298sw ✗ | 296sw ✗ | 593sw ✓ | 292sw ✓ | 484sw ✗ | 294sw ✓ | 597sw ✗ | 292sw ✓ | 11/20 |
| Qwen3.8-27B-UD-Q8_K_XL · - · 16k · default | 104s ✓ | 301s ✗ | 303s ✗ | 302s ✗ | 300s ✓ | 298s ✓ | 302s ✓ | 300s ✓ | 301s ✓ | 303s ✓ | 293s ✗ | 385s ✗ | 299s ✓ | 301s ✓ | 299s ✓ | 300s ✓ | 303s ✓ | 291s ✓ | 298s ✓ | 301s ✗ | 14/20 |
| Qwen3.8-27B-UD-Q8_K_XL · - · 32k · default | 307s ✓ | 301s ✗ | 301s ✗ | 297s ✓ | 300s ✓ | 300s ✓ | 300s ✓ | 333s ✗ | 300s ✓ | 300s ✓ | 298s ✓ | 298s ✓ | 300s ✓ | 303s ✗ | 301s ✓ | 301s ✓ | 303s ✓ | 382s ✓ | 299s ✓ | 298s ✓ | 16/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · - · 32k · guarded | 182s ✓ | 120s ✗ | 206s ✓ | 324s ✗ | 127s ✓ | 107s ✗ | 129s ✓ | 114s ✓ | 133s ✗ | 107s ✗ | 135s ✗ | 134s ✗ | 117s ✓ | 170s ✗ | 148s ✓ | 119s ✗ | 127s ✓ | 128s ✓ | 139s ✓ | 113s ✓ | 11/20 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · - · 16k · default | 185s ✓ | 139s ✗ | 127s ✗ | 121s ✓ | 155s ✓ | 167s ✓ | 165s ✓ | 112s ✓ | 132s ✗ | 180s ✓ | 130s ✓ | 131s ✗ | 111s ✗ | 126s ✓ | 123s ✓ | 143s ✗ | 121s ✓ | 110s ✓ | 199s ✓ | 175s ✓ | 14/20 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · - · 64k · default | 257s ✓ | 135s ✗ | 308s ✓ | 139s ✓ | 160s ✓ | 276s ✓ | 137s ✓ | 136s ✓ | 139s ✓ | 120s ✓ | 141s ✓ | 131s ✓ | 150s ✓ | 655s L | 129s ✓ | 150s ✓ | 115s ✓ | 139s ✓ | 188s ✓ | 117s ✓ | 18/20 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · - · 16k · default | 240s ✓ | 128s ✗ | 562s ✗ | 186s ✓ | 170s ✓ | 229s ✓ | 139s ✓ | 155s ✓ | 136s ✗ | 149s ✓ | 145s ✓ | 159s ✗ | 162s ✓ | 130s ✗ | 170s ✓ | 176s ✓ | 133s ✓ | 134s ✓ | 192s ✓ | 216s ✓ | 15/20 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · - · 32k · default | 105s ✓ | 147s ✗ | 408s ✓ | 205s ✓ | 167s ✓ | 86s ✓ | 161s ✓ | 156s ✓ | 163s ✓ | 137s ✗ | 121s ✓ | 141s ✗ | 157s ✗ | 151s ✓ | 202s ✓ | 177s ✗ | 148s ✓ | 137s ✓ | 195s ✓ | 176s ✓ | 15/20 |
| Ripple-65B-Preview-Q6_K · - · 16k · default | 716sw R | 899s L | 1339s L | 936s L | 720sw R | 1359s L | 1340s L | · | · | · | · | · | · | · | · | · | · | · | · | · | 0/7 (partial 7/20) |
| deepseek-v4.1-flash · - · 16k · default | 16sw ✗ | 21sw ✓ | 64sw ✓ | 17sw ✓ | 14sw ✓ | 30sw ✗ | 40sw ✗ | 20sw ✓ | 76sw ✓ | 14sw ✓ | 32sw ✓ | 20sw ✗ | 19sw ✓ | 45sw ✓ | 30sw ✗ | 15sw ✓ | 24sw ✓ | 14sw ✓ | 21sw ✓ | 52sw ✗ | 14/20 |
| gemma-4-31B-it-UD-Q8_K_XL · - · 16k · default | 406s ✗ | 407s ✗ | 460s ✗ | 537s ✗ | 518s ✗ | 416s ✗ | 428s ✗ | 503s ✗ | 423s ✗ | 375s ✗ | 518s ✗ | 427s ✗ | 162s ✗ | 239s ✗ | 480s ✗ | 467s ✗ | 424s ✗ | 402s ✗ | 431s ✗ | 455s ✗ | 0/20 |
