# Test protocol

> Living document. Updated after every run.
> Test files: [tasks_final.md](tasks/tasks_final.md) · [test2 spec](docs/test2_spec.md) · [README](README.md)

## 1. Setup

| Component | Value |
|---|---|
Endpoint | `http://192.168.1.111:21434` (aidir) |
Traffic tag | `X-Aidir-Client: openclaw-chain` (also `openclaw-batch`, `openclaw-v4`, `openclaw-shapes`) |
Models | `local-only` (currently Qwen3.8-27B-Q6_K_XL), previously Flash-Next IQ3_S |
Request parameters | `max_tokens=16000`, default temperature |
Ground truth | computed by code or by running the program, never by hand |

## 2. Rules

1. The same dataset is submitted to every model byte-for-byte identically.
2. `max_tokens` is never below 3000: Q6 produces long reasoning, and a small budget yields an empty answer — an artefact, not a model error.
3. Recorded for each item: date, seed, size, model (from the response `model` field), latency.
4. Model errors and harness errors are separated. Empty answers, timeouts and 5xx count as harness issues.
5. Results are stored as JSON next to the dataset; this protocol keeps only summaries and conclusions.

## 3. What is tested

- **Test 1.** 17 multi-hop tasks ([tasks_final.md](tasks/tasks_final.md)) mixed with same-type noise (`gen_noise.py`).
- **Test 2.** Program execution with decoy code in comments and strings (`gen_program*.py`).

## 4. Run log

| Date (HKT) | What | Model | Conditions | Result | Conclusion |
|---|---|---|---|---|---|
2026-11-03 | Stage 1: 24 tasks | Flash-Next IQ3_S | clean tasks, no noise | **24/24** | basic operations hold |
2026-11-03 | Stage 1: 24 tasks | Qwen3.8-27B Q6 | clean tasks, no noise | **24/24** | parity in accuracy |
2026-11-03 | Stage 2: 60 steps | Flash-Next IQ3_S | context ~20k, cache 99% | 60/60, 0 errors, 1.5 min | no degradation |
2026-11-03 | Stage 2: 60 steps | Qwen3.8-27B Q6 | context ~20k, cache 99% | 59/60, one 502, recall 0/3 at step 10 | possible glitch, needs retest |
2026-11-04 18:10 | Calibration (trial) | Q6 | max_tokens 700 and 3000 | almost all answers empty | budget too small: reasoning consumes it |
2026-11-04 18:25 | Calibration: dataset_20k | Q6 | max_tokens 6000 + retry | 6/6 without empties, one quality error (10 vs 6) | 6000 still tight, moved to 16k |
2026-11-04 18:37 | Calibration: dataset_20k | Q6 | max_tokens 16000, 126 KB, 300 noise lines | **10/17 (41% errors)**, no empties | close to the 50% target |
2026-11-04 18:49 | Batched run: all 17 in one request | Q6 | 129 KB, max_tokens 16000 | **4/17 (76% errors), 90 s** | batching sharply reduces accuracy |
2026-11-04 18:52 | Test 2: 8 programs (easy) | Q6 | ops=8, comments=300, extras=100, traps=30 | **8/8 (0% errors)** | too easy |
2026-11-04 19:10 | Test 2: v1 heavy | Q6 | ops=15, comments=800, extras=300, traps=80 | **7/8 (12% errors)** | still easy |
2026-11-04 19:10 | Test 2: v2 control flow | Q6 | ops=12, comments=600, extras=200, traps=60 | **7/8 (12% errors)** | next level needed |
2026-11-04 19:30 | Test 2: v3 nested | Q6 | ops=25, comments=1500, extras=500, traps=120 | **7/8 (12% errors)** | still easy |
2026-11-04 20:00 | Noise sweep: 2 shapes × 3 levels | Q6 | low/mid/high | **6/6 (0% errors)** | noise volume is not the lever |
2026-11-04 22:05 | Test 2: v4 × 5 programs | Q6 | ~106k tokens, ops=20, array + sum | **2/5 (60% errors)** | target reached and exceeded |
2026-11-04 22:11 | Language series (ru/en/zh) and v4 seeds 400–404 | Q6 | 8 tasks per language, ~106k tokens | **in progress** | language effect |

### Batch mode versus one-by-one

| Mode | Correct | Errors | Time |
|---|---|---|---|
One task per request | 10/17 | 41% | ~17 min |
All in one request | 4/17 | 76% | 90 s |

About eleven times faster, but twice as error-prone. Both modes are usable, but they must be **calibrated separately**; otherwise the scales are not comparable.

### Error profile (dataset_20k, Q6, 16k)

Failures: **2, 7, 9, 13, 14, 15, 17** — all requiring combination of rules and attributes: divisibility rules (2), mass + colour (7), counting by two features (9), ability + size (13), derived property (14), money trap (15), cancellation by order of mention (17).

Passed cleanly: **1, 3, 4, 6, 8, 10, 11, 12, 16** — all arithmetic chains, including long ones.

Conclusion: the model reliably sums offsets along a chain but loses rules when there are two and they must be selected or combined. This is exactly the skill required in agentic loops.

## 5. Observations and pitfalls

1. **Token budget is the main trap.** Q6 reasoning on a hard task takes **8–12 thousand characters** (≈3–4 thousand tokens), and more on difficult ones. At `max_tokens=700` or `3000` the answer is empty (`finish=length`). Working value: **16000**, with an automatic retry up to 32000 and a 2400 s request timeout.
2. **`reasoning_effort` barely matters.** Measured on one task with a 16k budget: `none` — 12,088 characters of reasoning, answer 0; `low` — 13,932, answer 10; `medium` — 14,458, answer 10; `high` — 14,919, answer 10. The length changes slightly, correctness does not.
3. **An empty answer is not a wrong answer.** They are counted separately. Example: task 2 with a full budget returned **10** instead of **6** — a genuine reasoning error.
4. **Routing.** `model: "qwen3.8-27b"` is a smart route that leads to another host running Q4. The exact id `Qwen3.8-27b-Q6_K_XL` is required for Q6; `local-only` currently points at Q6.
5. **Prefix cache.** Re-sending the same document yields `cached_tokens` ≈ 99.9% and response times below one second. A series of questions over one document barely loads prefill.
6. **Heartbeats.** System jobs cannot be disabled through the cron CLI. They defer under active traffic but may take a slot when idle.
7. **Concurrency.** Q6 reports `max_concurrent_requests: 2`; a third request waits.

## 6. Open questions

- Whether the language of a document shifts accuracy on rule-combination tasks.
- Whether Flash-Next shows a different error profile on the same calibrated files.
- How stable the calibrated difficulty is across restarts and cache states.

## 7. How to update

1. Append a row to the run log: date, dataset, model, conditions, result.
2. If a result is unexpected, add a note under Observations with the cause.
3. Reference result files as `[[name.json]]` in the Obsidian vault, or as plain paths in this repository.
