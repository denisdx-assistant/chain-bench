# Results

One folder per model, named exactly as the model is named in the runner config.
Inside each folder:

- `series.json` — machine-readable index of every run: file, test, language,
  budget, sample size, score, median latency, loop and length-cut counts;
- one JSON per run, named `<test>_<lang>_<budget>[_variant].json`.

Model names are exact and must not be shortened (see the registry in the root
README). A new run never overwrites an old one: it gets a new file or a new
folder.

## Qwen3.8-27B-UD-Q6_K_XL

| Run file | Test | Lang | Budget | Correct | Errors | Median latency | Median reasoning | Length cuts |
|---|---|---|---|---|---|---|---|---|
| `chains_ru_20k_16k.json` | chains, full 17 | ru | 16k | 10/17 | 41% | 61 s | 11.9k chars | 0 |
| `chains_ru_20k_16k_8tasks.json` | chains, 8-task subset | ru | 16k | 4/8 | 50% | 45 s | 7.1k chars | 0 |
| `chains_en_20k_16k.json` | chains, 8-task subset | en | 16k | 4/8 | 50% | 48 s | 8.9k chars | 0 |
| `chains_zh_20k_16k.json` | chains, 8-task subset | zh | 16k | 5/8 | 38% | 33 s | 2.1k chars | 0 |
| `programs_v4_16k.json` | programs v4, 20 | — | 16k | 11/20 | 45% | 296 s | n/a | 0 |
| `programs_v2_flow_8.json` | programs v2 flow, 8 (legacy) | — | 16k | 7/8 | 12% | 60 s | 6.3k chars | 0 |
| `programs_v2_hard_8.json` | programs v2 hard, 8 (legacy) | — | 16k | 7/8 | 12% | 88 s | 7.6k chars | 0 |

## Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1M

| Run file | Test | Lang | Budget | Correct | Errors | Median latency | Median reasoning | Length cuts |
|---|---|---|---|---|---|---|---|---|
| `chains_ru_20k_65535.json` | chains, full 17 | ru | 65535 | 12/17 | 29% | 83 s | 23.7k chars | 0 |
| `chains_ru_20k_32k_guarded.json` | chains, full 17 | ru | 32k | 10/17 | 41% | 82 s | n/a | 1 |
| `chains_ru_20k_task12_retry_131k.json` | chains, retry of task 12 | ru | 131072 | 1/1 | 0% | 214 s | n/a | 0 |
| `programs_v4_32k_guarded.json` | programs v4, 20 | — | 32k | 3/20 | 85% | 129 s | 14.1k chars | 3 |

The 65535 run used default sampling. The 32k run used temperature 0.3,
frequency/presence penalty 0.3, and the streaming loop guard.

## Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S

Base weights without YaRN, served as the 262k context variant.

| Run file | Test | Lang | Budget | Correct | Errors | Median latency | Median reasoning | Length cuts |
|---|---|---|---|---|---|---|---|---|
| `programs_v4_32k_guarded.json` | programs v4, 20 | — | 32k | 2/20 | 90% | 130 s | 15.3k chars | 2 |

## `_invalid/`

Runs kept for the record but not used as evidence. Both are batch runs where a
single request was asked to answer all 17 chain tasks at once:

- `chains_ru_batch_chunked.json` — 4/17. Answers were parsed from a multi-task
  response; parsing, not the model, decided the score.
- `chains_ru_batch_chunked_next.json` — 0/17. The request hit the length cap
  (97.8k chars of reasoning) and returned empty content.

They are excluded from all tables and from the score aggregates.

## Metric definitions

- **Correct** — answer matches the expected value exactly. For programs, both
  the final array (element by element) and the sum must match.
- **Errors** — 100% minus the share of exact matches. No partial credit.
- **Median latency** — wall-clock seconds per task, including time spent
  waiting in the local model queue. It is not pure inference time.
- **Median reasoning** — median character count of `reasoning_content`.
  Comparable only within the same task set.
- **Length cuts** — responses that ended with `finish_reason = length`.
- **Loops** — responses aborted by the guard because a repeated 8-word window
  appeared more than 40 times. Counted separately from ordinary wrong answers.
