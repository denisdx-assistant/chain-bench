# chain-bench

**A private benchmark for local language models: multi-hop chains and program
execution under noise.**

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

**What it shows.** Q6 is the strongest on both tests. Flash-Next variants are
comparable on chains at a large budget but three to five times worse on program
execution. The base 262k variant and the YaRN 1M variant differ within the noise
of a single run, so YaRN is not what costs accuracy. Degenerate loops are rare
and are contained by a streaming guard rather than by a bigger budget.

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
8-task subset instead of the full set. Regenerated from result files.

<!-- summary:start -->
| Run | Overall | Test 1 en | Test 1 ru | Test 1 zh | Test 2 |
|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default · budget 16k | 28m57s 42% | 5m19s 4/8 (8) | 13m30s 10/17 | 10m08s 5/8 (8) | — |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · budget 16k · guard | 30m22s 38% | 14m42s 11/17 | 15m40s 10/17 | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · ctx 262k · no YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 54m01s 90% | — | — | — | 54m01s 2/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 94m29s 65% | — | 30m21s 10/17 | — | 64m08s 3/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T default · budget 65535 · provenance inferred | 27m58s 29% | — | 27m58s 12/17 | — | — |
<!-- summary:end -->

**Details.**

- Per-task matrices, every task with its own time and result:
  [docs/results-by-task.md](docs/results-by-task.md)
- Per-run tables with reasoning sizes and length cuts:
  [results/README.md](results/README.md)
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

## License

Code — MIT. Texts and datasets — CC BY 4.0.
