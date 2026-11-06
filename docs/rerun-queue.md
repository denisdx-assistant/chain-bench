# Rerun queue: tasks cut off by the token budget

A row that ends with `finish=length` did not finish thinking: the answer was
truncated, so its `ok=false` measures the budget, not the model. Such rows are
the only ones queued for a targeted rerun at a larger budget.

Scope: every canonical run under `results/`. Archived and `_invalid` folders are
excluded — they are kept for history, not for scoring.

Rerun rule: same dataset, same sampling, budget `131072`, one task at a time,
output to `<original-name>_retry_131k.json`. The original file is never
overwritten; the retry is recorded next to it and referenced from the series.

## Queue

| # | Model | Run | Task | Why | Status |
|---|---|---|---|---|---|
| 1 | `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M` | `chains_ru_20k_32k_guarded.json` | chain 12 | `finish=length` at 32k, 379 s | ✅ done — `chains_ru_20k_task12_retry_131k.json`, answer 100 = expected 100 |
| 2 | `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M` | `programs_v4_32k_guarded.json` | `v4_seed313.py` | `finish=length` at 32k, 385 s | ⬜ pending |
| 3 | `Qwen3.8-Flash-Next-UD-Q4_K_XL` | `programs_v4_16k.json` | `v4_seed302.py` | `finish=length` at 16k, 395 s | ⬜ pending |
| 4 | `Qwen3.8-Flash-Next-UD-Q4_K_XL` | `programs_v4_16k.json` | `v4_seed310.py` | `finish=length` at 16k, 475 s | ⬜ pending |

Pending items need the model to be loaded on a host; they are run together the
next time it is up.

## Checked and not queued

Every other run was scanned for `finish=length`; the following have none, so no
rerun is needed:

- `Qwen3.8-27B-UD-Q4_K_M` — chains ru/en/zh, subsets, programs
- `Qwen3.8-27B-UD-Q6_K_XL` — chains ru/en/zh, subsets, programs
- `Qwen3.8-27B-UD-Q8_K_XL` — both the archived 16k series and the 32k
  reproduction run
- `Qwen3.8-Flash-Next-UD-IQ4_XS` — chains ru/en/zh, subsets, programs
- `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M` — chains en/zh, all subsets
- `Qwen3.8-Flash-Next-UD-Q4_K_XL` — chains ru/en/zh, all subsets

A short or empty-looking `raw` is not by itself a truncation. In program runs a
missing answer means the reply carried no code block (a format failure, scored
`kind=wrong`), and in chain runs it means the model emitted a short wrong number
with `finish=stop`. Neither is a budget artefact.

## After a rerun

1. Score the retry row; if it is correct, the model's ceiling for that run rises
   by one task.
2. Keep both numbers visible: the measured run stays as it was, and the retry is
   cited in `results/run-configs.json` under the same model.
3. Do not blend a retry into a different run's totals.
