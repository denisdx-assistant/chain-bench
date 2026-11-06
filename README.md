# chain-bench

**A contamination-free benchmark for local language models: multi-hop chains and
program execution under noise.**

Languages: **English** · [Русский](README.ru.md) · [中文](README.zh.md)

---

## Abstract

**Why this exists.** Two goals:

1. Build and validate a cheap, reproducible methodology for comparing local
   models, with automatic difficulty adjustment — the suite is tuned so that a
   reference model fails about half the time, which is where a test still
   discriminates.
2. Use it to choose the best model for a host with **2× V100 32 GB and 128 GB
   RAM**, where the trade-off between quantisation, context mode and speed
   decides what is practical.

**What was done.** Two tests were built and frozen: 17 multi-hop arithmetic
chains inside a 20k-token noise document (three languages), and mental execution
of 20 Python programs whose comments contain code that never runs. Ground truth
is computed by code. Difficulty was calibrated on
`Qwen3.8-27B-UD-Q6_K_XL` to 41% errors on chains and 45% on programs, close to
the 50% target. Series were then run for three Flash-Next configurations and for
`Qwen3.8-27B-UD-Q8_K_XL`.

**What it shows.** On chains the models are **not** separated: Q6 10/17,
Flash-Next 12/17 at a large budget and 10/17 at 32k, Q8 10/17 on Russian and
11/17 on English — one or two tasks apart on a 17-task set, well inside the
interval. YaRN 1M and the 262k base differ by one program, also inside noise.
Degenerate loops are rare and are contained by a streaming guard rather than by
a bigger budget.

## 1. Methodology

**Test 1 — chains in noise.** A ~20k-token document of semantically neutral
noise (300 lines, ~72k characters) contains statement chains and 17 questions.
The answer is a single integer. The same generator and seed are used for each
language, so the noise is parallel and only the language changes.

**Test 2 — frozen programs.** 20 Python programs (seeds 300–319) build a
10-element array with swaps, branches, loops, recursion, regex, type coercion
and aliasing. Comments and strings contain decoy code. The model returns the
final array and its sum; both must match exactly.

**Calibration.** Difficulty is raised by structural complexity first and noise
volume second; a small token budget is deliberately not used as a lever. The
reference model is tuned to roughly 50% errors. The full step-by-step table is
in [docs/calibration.md](docs/calibration.md).

**Controls.** One task per request; a documented budget per model class; a
streaming loop guard that aborts degenerate repetition; retries for length cuts
at four times the budget; provenance recorded with every run. Rules are in
[docs/methodology.md](docs/methodology.md).

**Artifacts.**

- Datasets and SHA-256 hashes: [datasets/MANIFEST.json](datasets/MANIFEST.json)
- Generators: [scripts/gen_noise.py](scripts/gen_noise.py),
  [scripts/gen_program_v3.py](scripts/gen_program_v3.py),
  [scripts/build_i18n_all.py](scripts/build_i18n_all.py)
- Runners: [scripts/run_chains_guarded.py](scripts/run_chains_guarded.py),
  [scripts/run_frozen_guarded.py](scripts/run_frozen_guarded.py)
- Loop guard: [scripts/guard.py](scripts/guard.py)
- Scoring self-test: [scripts/selftest_scoring.py](scripts/selftest_scoring.py)
- Re-score saved answers: [scripts/rescore.py](scripts/rescore.py)

## 2. Test series

**Datasets.** Test 1: a full 17-task document in Russian, English and Chinese,
plus an 8-task translated subset kept for continuity with the first runs. Test 2:
one frozen set of 20 programs, no language split. All sets are frozen; a new
variant is added as a new file.

**How the series was run.** Each model is served through one local endpoint, so
runs are strictly sequential. A run is one task per request, with the budget and
sampling recorded in [results/run-configs.json](results/run-configs.json). A
model may occupy several rows below when it was served with a different context,
YaRN setting, temperature or budget — the serving context is 262k unless the
name says otherwise (`+ YaRN 1M`).

**Adjustment in practice.** Chains were tuned by adding rule-combination tasks
and by keeping noise at 20k tokens, after a sweep showed that 40k and 60k do not
move accuracy. Programs were tuned by adding operations, nesting and decoys
across four generations until the reference model dropped to about half wrong.

### Summary

Each cell is one test series: total wall-clock time and score. `(8)` marks the
8-task subset instead of the full set. Regenerated from result files. A configuration
run more than once shows the mean over its valid runs, so a cell can be fractional
(`11.5/17`): the first run and its reproduction both count.


<!-- summary:start -->
| Run | Overall (errors) | Median tokens/task | Test 1 en (correct) | Test 1 ru (correct) | Test 1 zh (correct) | Test 1 subsets 8 (all langs) | Test 2 (correct) |
|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M · ctx 200k · no YaRN · T default · guard | 293m25s · 31% err | 4034 | 108m21s 12/17 | 93m16s 11/17 | 91m48s 12/17 | 22m14s 12/24 | — |
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default | 165m59s · 35% err | 4099 | 14m06s 13/17 | 13m30s 10/17 | 16m44s 12/17 | 20m11s 13/24 | 121m39s 11/20 |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · guard | 146m44s · 33% err | 4100 | 14m14s 11/17 | 14m45s 10/17 | 17m43s 11.5/17 | 15m10s 13/24 | 100m03s 15/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ctx 1M · YaRN · T 0.3 · pen 0.3 · guard | 137m55s · 38% err | 4899 | 24m51s 12/17 | 30m21s 10/17 | 31m10s 11/17 | 13m15s 15/24 | 51m33s 11/20 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ctx 1M · YaRN · T default · pen 0.2 · guard | 127m31s · 30% err | 5960 | 26m38s 12/17 | 26m24s 11/17 | 26m57s 13/17 | 19m29s 15/24 | 47m32s 14/20 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ctx 1M · YaRN · T default · pen 0.2 · guard | 162m02s · 27% err | 4958 | 32m51s 13/17 | 29m33s 11/17 | 35m27s 14/17 | 25m52s 15/24 | 64m11s 14/20 |
| gemma-4-31B-it-UD-Q8_K_XL · ctx 262k · no YaRN · T default · guard | 168m44s · 58% err | 1601 | 11m40s 9/17 | 7m24s 10/17 | 8m22s 11/17 | 11m17s 14/24 | 141m18s 0/20 |
<!-- summary:end -->

**Details.**

- Per-task matrices, every task with its own time and result:
  [docs/results-by-task.md](docs/results-by-task.md)
- Per-run tables with reasoning sizes and length cuts:
  [results/README.md](results/README.md)
- Performance per run, from server timings: generation and prefill speed, tokens
  spent per task: [docs/performance.md](docs/performance.md)
- Context-length prefill (261k / 512k / 1M tokens):
  [docs/context-prefill.md](docs/context-prefill.md)
- Serving hardware and KV-cache settings per host:
  [docs/hardware.md](docs/hardware.md)
- Chronological log of runs and calibration:
  [docs/run-log.md](docs/run-log.md)

## 3. Models

Exact names as used in the runner configuration; short forms are not used in
tables.

| Model | Status |
|---|---|
| `Qwen3.8-27B-UD-Q6_K_XL` | measured |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m` | measured |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S` | measured |
| `Qwen3.8-27B-UD-Q8_K_XL` | in progress |
| `Qwen3.8-Flash-Next-UD-Q4_K_XL` | queued: YaRN 1M, 32k guarded |
| `Qwen3.8-Flash-Next-UD-IQ4_XS` | queued: YaRN 1M, 32k guarded |
| `Qwen3.8-Flash-Next-IQ3_M` | planned |

## 4. Reproducing a run

```bash
python3 scripts/run_chains_guarded.py \
    --dataset datasets/chains/ru/dataset_20k_17tasks.json \
    --model local-only --max-tokens 16000 --timeout 2400 --temp -1 \
    --out results/<model>/chains_ru_20k_16k.json

python3 scripts/run_frozen_guarded.py --dir datasets/programs/v4 \
    --model local-only --max-tokens 16000 --timeout 2400 --temp -1 \
    --out results/<model>/programs_v4_16k.json
```

`--temp -1` means default sampling: the field is omitted rather than set to a
value. Generators are deterministic by seed.

## 5. Limitations

- Small samples: 17 chains and 20 programs. The value is in error profiles and
  relative ordering, not in precise rates.
- One hardware configuration and one local endpoint; median latency includes
  queue time.
- The 8-task trilingual subset is a legacy cross-check, not a full translation
  of the first generation.
- The three planned quantisations have no runs yet.

## 6. Repository layout

```
README.md            this file (English, primary)
README.ru.md         Russian translation
README.zh.md         Chinese translation
docs/                methodology, calibration, per-task results, run log (English)
datasets/            frozen data + MANIFEST.json with SHA-256
results/             one folder per model, exact model name
  <model>/series.json    machine-readable index of runs
  <model>/*.json         one file per run
results/run-configs.json  serving configuration per run
results/_invalid/    batch experiments kept for the record, excluded from tables
scripts/             generators, runners, loop guard, table builder
```

**Note on program scores.** An earlier guarded runner compared answers against
`array`/`sum` keys while the datasets store `expected_array`/`expected_sum`, so
every program in those runs was scored wrong. The affected runs (Flash-Next
variants) are withdrawn from the tables and are being re-run with the fixed
comparison; Q6's program score is reproducible from its stored answers.

## Published data
## Published data

The repository is public. It contains the frozen datasets, the harness and all
results. Endpoint addresses in the scripts are placeholders for a local model
server; no credentials, keys or private corpora are included.

## License

Code — MIT. Texts and datasets — CC BY 4.0.
