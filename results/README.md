# Results

One folder per model, named exactly as the model is named in the runner config.
Inside each folder:

- `series.json` — machine-readable index of the runs: file, test, language,
  budget, sample size, score, median latency, median speed, token counts, loop
  and length-cut counters;
- one JSON per run, named `<test>_<lang>_<budget>[_variant].json`;
- the matching `.log` files (not tracked) hold the per-task lines.

A run is append-only: the runner refuses to overwrite an existing file unless it
is explicitly continued with `--resume` or forced with `--force`.

## Where the numbers live

Do not read the tables below from memory — they are generated:

- `docs/performance.md` — speed per run: best and median generation, best
  prefill (uncached only), answer and prompt tokens, compute time;
- `docs/results-by-task.md` — per-task matrix: every task with its own time and
  verdict;
- `README.md` (section 6.5) — the summary matrix, one row per run configuration;
- `docs/hardware.md` — hosts, engines and KV-cache settings.

## Archive

`_archive/` holds runs that are not comparable with the main matrix:

- `programs_v2_flow_8.json`, `programs_v2_hard_8.json` — earlier 8-program sets
  generated with a different program generator, kept for history only;
- `chains_ru_20k_65535.json` — early chains run at a 65535 budget with default
  sampling and without a recorded resolved model; superseded by the guarded 32k
  series.

`_invalid/` holds experiments that never produced a valid score: batch runs that
asked one request to answer every task, and runs whose scoring could not be
reproduced.
