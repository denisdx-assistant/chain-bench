# chain-bench

**A private benchmark for local language models: multi-hop chains and program
execution under noise.**

Languages: **English** · [Русский](README.ru.md) · [中文](README.zh.md)

---

## Abstract

Public benchmarks suffer from contamination: a model may have seen the tasks
during training. This suite measures something else — the ability to **hold
dependencies together**. Test 1 embeds multi-hop arithmetic chains in a long
document of semantically neutral noise; Test 2 asks the model to mentally
execute a small Python program whose comments and strings contain code that is
never executed. Ground truth is always computed by code, never by hand.

The project has two separate aspects:

1. **The harness** — a reusable methodology: frozen datasets, recorded
   provenance, a loop guard, a strict retry policy for length cuts, and results
   stored per model. It is designed so that a later run on another machine is
   comparable with an earlier one.
2. **Current results** — a small, honest snapshot of how three
   quantisations/configurations actually behave. Sample sizes are deliberately
   modest; the value is in the error profile, not in the third significant
   digit.

## 1. What is measured

Two skills that matter for agent loops and that public benchmarks do not
isolate:

- **Rule combination under noise.** Summing offsets along a chain is easy;
  selecting and combining two rules while thousands of near-duplicate
  statements surround them is not.
- **Mental execution of code.** Comments and string constants that contain
  plausible code are a direct trap for a model that reads rather than executes.

Accuracy and wall-clock latency are both recorded. Degenerate behaviour (loops,
length cuts) is counted separately from ordinary wrong answers.

## 2. Test 1 — arithmetic chains in noise

- A document of roughly 20k tokens (300 noise lines, ~72k characters) is
  generated from the same generator and seed for every language. The noise is
  semantically neutral: the same predicates applied to other entities,
  near-duplicate identifiers, group rules about other classes. Entity names
  from the tasks never appear in the noise.
- 17 tasks cover sums of offsets, divisibility rules, star-shaped min/max,
  branching, age with aliases, sequential percentages, mass and colour
  thresholds, mileage with divisibility, counting by two features, ratios,
  rule priority, group versus group, ability and size, derived properties, a
  money trap, variable mutation, and cancellation by order of mention.
- The answer is a single integer. Ground truth is computed by code.

## 3. Test 2 — frozen programs

- 20 Python programs (seeds 300–319) build a 10-element integer array with
  swaps, `+=`, `-=`, `*=`, slice sorting, reversal, conditionals, loops,
  recursion, regular expressions, type coercion with `str(a) + str(b)`, and
  aliasing (`arr2 = arr`).
- Noise is code inside comments and string constants that is never executed.
- The model returns the final array and its sum in a fixed format
  (`ARRAY: [...]`, `SUM: n`). Both must match exactly; there is no partial
  credit.
- The set is frozen: every model sees byte-identical input.

## 4. Harness rules

| Rule | Value |
|---|---|
| One task per request | always for scoring; batch runs are kept as invalid experiments |
| Loop guard | streamed 8-word shingles; abort when one shingle repeats > 40 times, mark `kind=loop` |
| Sampling for guarded runs | temperature 0.3, `frequency_penalty` 0.3, `presence_penalty` 0.3 |
| Budget, 27B class | 16k |
| Budget, Flash-Next class | 32k with the guard |
| Length-cut retry | re-run at 4× budget (131072), reported next to the original |
| Provenance | router queried before the run; `resolved_provider` and `resolved_model` stored in the result |
| Empty answer | counted as a harness artefact, never as a model error |

**Budget is a parameter, not a detail.** Too small a budget turns a capable
model into an empty answer: reasoning alone can exceed it. A budget that is too
large does not help a loop: a loop consumes any budget. The measured correction
is that long generations on hard tasks were often degenerate repetition, so the
lever is loop control plus a moderate budget, not a bigger cap.

## 5. Datasets (frozen 2026-11-05)

`datasets/MANIFEST.json` records the exact files, sizes and SHA-256 hashes.
Frozen data is never edited; a new variant is added as a new file.

| Set | Language | Tasks | Document | Note |
|---|---|---|---|---|
| `chains/ru/dataset_20k_17tasks.json` | ru | 17 | 20k tokens, 300 noise lines | full set |
| `chains/ru/dataset_20k_8tasks.json` | ru | 8 | same document, same tasks 1–8 | trilingual subset |
| `chains/en/dataset_20k_8tasks.json` | en | 8 | translated document and tasks | trilingual subset |
| `chains/zh/dataset_20k_8tasks.json` | zh | 8 | translated document and tasks | trilingual subset |
| `chains/en/dataset_20k_17tasks.json` | en | 17 | translated document and tasks | full set, added 2026-11-05 |
| `chains/zh/dataset_20k_17tasks.json` | zh | 17 | translated document and tasks | full set, added 2026-11-05 |
| `programs/v4/` | — | 20 | 20 `.py` + expected `.json` | no language split |

Coverage is now symmetric for the full set: all three languages have a 17-task
document. The Russian set was produced by the original noise generator; the
English and Chinese 17-task sets use the trilingual generator at seed 21 and the
same noise parameters (20 000 tokens, 300 lines), so they are parallel to each
other. Russian and non-Russian full sets differ in noise wording by construction;
the 8-task translations are kept as the earlier frozen subset.

## 6. Results

### 6.1 Test 1, full 17-task set (Russian, one task per request)

| Model | Lang | Budget | Correct | Errors | Median latency | Median reasoning | Length cuts | Loops |
|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL | ru | 16k | 10/17 | 41% | 61 s | 11.9k chars | 0 | 0 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m | ru | 65535, default sampling | 12/17 | 29% | 83 s | 23.7k chars | 0 | 0 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m | ru | 32k, guarded | 10/17 | 41% | 82 s | — | 1 | 0 |
| Qwen3.8-27B-UD-Q6_K_XL | en | 16k | — | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL | zh | 16k | — | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m | en | 32k, guarded | — | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m | zh | 32k, guarded | — | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | ru | 32k, guarded | — | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | en | 32k, guarded | — | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | zh | 32k, guarded | — | — | — | — | — | — |

Rows with dashes are frozen sets that have not been run yet. They are kept in the
table so that results land in a fixed place.

The 32k guarded run is the only one where one task hit the cap (task 12). A
separate retry of that task at 131072 returned the correct value in 214 s,
which classifies it as a genuine long reasoning case, not a loop.

### 6.2 Test 1, 8-task trilingual subset

| Model | Language | Budget | Correct | Errors | Median latency |
|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL | ru | 16k | 4/8 | 50% | 45 s |
| Qwen3.8-27B-UD-Q6_K_XL | en | 16k | 4/8 | 50% | 48 s |
| Qwen3.8-27B-UD-Q6_K_XL | zh | 16k | 5/8 | 38% | 33 s |

### 6.3 Test 2, 20 frozen programs

| Model | Budget | Correct | Errors | Median latency | Median reasoning | Length cuts | Loops |
|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL | 16k | 11/20 | 45% | 296 s | — | 0 | 0 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1M | 32k, guarded | 3/20 | 85% | 129 s | 14.1k chars | 3 | 0 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S | 32k, guarded | 2/20 | 90% | 130 s | 15.3k chars | 2 | 0 |

Speed here is median wall-clock seconds per task, including queue time. It is
not pure inference throughput and should not be compared with vendor numbers.

### 6.4 Calibration findings (context, not scored)

- Batch mode — all 17 chain tasks in one request — is about eleven times
  faster but roughly twice as error-prone (4/17, 76%). It is excluded from
  scoring.
- Raising noise volume from 20k to 65–100k tokens did not raise the error rate;
  structural complexity did.
- `reasoning_effort` changes reasoning length (12.1k → 14.9k characters) but
  not correctness.

<!-- per-task:start -->
## 6.5 Summary and per-task results

The first table is the summary: one row per run configuration, one column per
test group, each cell is the total wall-clock time of that series and its score.
A model may appear in several rows when it was served with a different context,
YaRN setting, temperature or budget; the row label carries the configuration.
The tables below give the same runs task by task.
Everything here is generated from the result files and `results/run-configs.json`
by `scripts/build_task_tables.py`; do not edit by hand.

### Summary by test group

Cell format: total wall-clock time of the group and correct/total.

`(8)` marks a run on the 8-task subset instead of the full set.

| Run | Overall | Test 1 en | Test 1 ru | Test 1 zh | Test 2 |
|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default · budget 16k | 28m57s 42% | 5m19s 4/8 (8) | 13m30s 10/17 | 10m08s 5/8 (8) | — |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · budget 16k · guard | 15m40s 41% | — | 15m40s 10/17 | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ctx 262k · no YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 54m01s 90% | — | — | — | 54m01s 2/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 94m29s 65% | — | 30m21s 10/17 | — | 64m08s 3/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T default · budget 65535 | 27m58s 29% | — | 27m58s 12/17 | — | — |

### Test 1 — full 17-task set

| Run | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | T15 | T16 | T17 | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ru · 16k · default | 23s ✓ | 78s ✗ | 10s ✓ | 8s ✓ | 9s ✓ | 7s ✓ | 73s ✗ | 9s ✓ | 68s ✗ | 51s ✓ | 73s ✓ | 70s ✓ | 62s ✗ | 73s ✗ | 61s ✗ | 74s ✓ | 61s ✗ | 10/17 |
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

<!-- per-task:end -->

## 7. Qualitative comparison

1. **Q6 is the strongest of the three on both tests.** It is also the slowest on
   programs (296 s median), because it thinks longer before committing.
2. **Flash-Next is not simply "Q6 with less budget".** On test 2 its failures
   are confident wrong answers with 11–16k characters of reasoning and
   `finish=stop`, not starvation. On test 1 its accuracy is comparable to Q6 at
   a large budget, which suggests the program-execution task is where the gap
   really is.
3. **YaRN is not the cause of degradation.** The base 262k variant scored 2/20
   against 3/20 for the YaRN 1M variant on the same frozen set — a difference
   inside the noise of one run. Removing YaRN did not recover accuracy.
4. **The cap matters only where the model succeeds.** In test 2 the length cuts
   coincide with correct answers on both Flash-Next variants: a model that
   knows the answer reasons long enough to hit 32k; a model that does not
   answers quickly and wrongly.
5. **Loops are rare, and controllable.** The guard never fired in the scored
   runs with penalties at 0.3. The one loop observed earlier (before the guard)
   repeated a single noise block verbatim and consumed the entire budget.
6. **Error profile is stable across models.** On test 1 the same task types
   fail: rule combination, attribute selection, cancellation by order of
   mention. Plain arithmetic chains pass.

## 8. Model registry

Exact names as used in the runner configuration. Short forms are not permitted
in results or tables.

| Model | Status | Runs |
|---|---|---|
| `Qwen3.8-27B-UD-Q6_K_XL` | measured | test 1 (ru 17, ru/en/zh 8), test 2 (20) |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m` | measured | test 1 (ru 17, two budgets), test 2 (20) |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S` | measured | test 2 (20) |
| `Qwen3.8-Flash-Next-UD-Q4_K_XL` | planned | — |
| `Qwen3.8-Flash-Next-UD-IQ4_XS` | planned | — |
| `Qwen3.8-Flash-Next-IQ3_M` | planned | — |
| `Qwen3.8-27B-UD-Q8_K_XL` | planned | — |

## 9. Reproducing a run

```bash
# one task per request, guarded, provenance recorded
python3 scripts/run_chains.py --dataset datasets/chains/ru/dataset_20k_17tasks.json \
    --model local-only --max-tokens 32000 --timeout 900 --temp 0.3 --fp 0.3 --pp 0.3 \
    --out results/<model>/chains_ru_20k_32k_guarded.json

# frozen programs, same guard
python3 scripts/run_frozen_guarded.py --dir datasets/programs/v4 --model local-only \
    --max-tokens 32000 --timeout 900 --temp 0.3 --fp 0.3 --pp 0.3 \
    --out results/<model>/programs_v4_32k_guarded.json
```

Generators are deterministic by seed: identical parameters produce
byte-identical data.

## 10. Repository layout

```
README.md            this file (English, primary)
README.ru.md         Russian translation
README.zh.md         Chinese translation
docs/methodology.md  the harness as an artifact: rules, guard, retry policy
docs/run-log.md      chronological log of runs and calibration
datasets/            frozen data + MANIFEST.json with SHA-256 hashes
  chains/{ru,en,zh}/ noisy documents and tasks
  programs/v4/       20 frozen programs with expected arrays and sums
results/             one folder per model, exact model name
  <model>/series.json    machine-readable index of runs
  <model>/*.json         one file per run
results/_invalid/    batch experiments kept for the record, excluded from tables
scripts/             generators, runners, loop guard
```

## 11. Limitations

- Small samples: 17 chains and 20 programs. Conclusions concern error profiles
  and relative ordering, not precise rates.
- One hardware configuration (2× V100, single local endpoint).
- Median latency includes queue time and is affected by concurrency.
- The trilingual coverage is an 8-task subset, not the full 17.
- The four planned quantisations have no runs yet; their rows exist so that
  results land in a fixed place.

## License

Code — MIT. Texts and datasets — CC BY 4.0.
