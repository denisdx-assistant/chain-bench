# Pending runs

**Status 2026-09-11: paused, not finished.** The owner stopped the programme until Qwen4
ships ("на днях"). Nothing should start on its own. Ripple-65B is dropped for good: too
heavy for the hardware and not smart enough to be worth the hours — revisit only if it
becomes interesting again.

Parked behind the pause:

- large-context speed probes for the 27B trio, IQ1_M, gemma and Ripple;
- the 5k prefill point for every model (all datasets start at ~14k tokens);
- a full series for Orca Q1 — **cancelled 2026-11-09**: the model is clearly too weak and
  the existing run is reference enough;
- Ripple: ruined by the decision above, so its missing languages and 13 programs will
  not be computed.

Work agreed with the owner and not yet executed. Kept here so nothing is lost
between sessions.

## 1. Qwen3.8-Flash-Next-UD-Q4_K_XL — programs at 64k

Reason: the first two runs used a 32k budget and only the cut tasks were retried at
64k, while IQ4_XS ran all 20 programs at 64k and scored 18/20. To compare the two
in identical conditions, run the whole program set at 64k.

- script: `/tmp/q4kxl_programs_64k.sh`
- output: `results/Qwen3.8-Flash-Next-UD-Q4_K_XL/programs_v4_64k_rerun.json`
- expected duration: about an hour
- needs: `local-only` pointed at this model

## 2. Qwen3.8-Flash-Next-Orca-Abliterated (Q1) — full reference series

Abliterated Q1 build of Flash-Next with part of the experts removed. Runs on very
weak hardware; we will still serve it on two cards.

Vendor defaults must be used, not our usual sampling:

```
--temp 0.6 --top-p 0.95 --min-p 0.05 --repeat-penalty 1.05 --presence-penalty 0.5
```

The runner now forwards `top_p`, `min_p` and `repeat_penalty`; `presence_penalty`
goes as `--pp 0.5`. Budget 64k, timeout one hour, guard on. Duplicated requests are
acceptable on this model.

- script: `/tmp/series_orca_q1.sh` — takes the model name from `local-only`, so the
  folder name matches whatever id the server reports
- output: `results/<model>/chains_{ru,en,zh}_20k_64k.json`, `..._8tasks.json`,
  `programs_v4_64k.json`
- needs: model added to aidir and `local-only` pointed at it

Both runs are strictly sequential: one model is loaded at a time.

## 3. Large-context prefill needs the prompt cache off

`scripts/speed_probe.py` builds an instruction-first prompt and filler sized to a
target, but the server serves almost all of it from its prompt cache even when every
filler line carries a unique number: the last attempt reported `prompt_n = 5` with
the rest cached. Generation speed is unaffected and already measured (83 / 84 / 67
t/s at 181k / 425k / 815k of prompt). Prefill at these sizes can only be measured
with prompt caching disabled on the server side, or by reading `prompt_ms` of a
genuinely cold request.

## Qwen3.8-Flash-Next-Abiray-Coder-IQ1_M (running)

Full series at a 32k budget, launched 17:22 HKT from `/tmp/series_iq1m.sh`:
chains en/ru/zh (17 tasks), the three 8-task subsets, then programs v4 (20 tasks).

Two things are specific to this model:

- it **understands Russian but does not answer in it**, so the Russian chains measure
  reasoning, not language. The answers will be English and the ru column must be read
  with that in mind.
- `local-only` is disabled, so the runner addresses the model by its own id
  (`qwen3.8-flash-next-abiray-coder-iq1_m`); the provider is
  `local_qwen3.8-flash-next-abiray-coder-iq1_m`.

### Parallel run planned: Chinese chains with two clients

This provider batches up to two requests, so after the sequential series the Chinese
chains are repeated with `scripts/run_chains_parallel.py --workers 2`. Nothing in the tasks changes; only the arrival pattern does.

The result is a separate file, `chains_zh_20k_32k_par2.json`, and it answers a different
question than the sequential run: how far per-request generation falls when two streams
share the GPU, and whether aggregate throughput rises despite that. Rows carry
`start_ts`/`end_ts` and `concurrent_peers`, so batched and unbatched rows can be told apart
without guessing.

**Result.** Two clients made it worse, not better: per-stream generation fell from 83.2 to
59.2 t/s and aggregate throughput from 78.3 to 72.3 tok/s, with the series 8% longer. All 17
rows of the two-client run genuinely overlapped another request. One stream already
saturates memory bandwidth, so the provider's batch of two buys nothing for this model.

Programs finished at 0/20 with 12 length cuts and 1.04M tokens written: the IQ1_M quant is
not usable for code at this task size.

## 4. Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S — full replicate for statistics

Owner asked for a second complete sample to see run-to-run spread rather than a new
record. Sampling matches the first sample (temperature 0.3, penalties 0.3, YaRN 1M); the
budget is 65536 instead of 32k, which does **not** break the comparison: the budget is only a
cutoff, and any task it cut was rerun separately at a larger limit. So the two samples are
interchangeable and the table averages them into one row. Chain sets, the three 8-task
subsets and all 20 programs. A first attempt at 32k ran 7 English tasks and was archived to
`results/_archive/IQ3S_32k_rep2_partial`.

- provider renamed by the owner to `ista-iq3_s` (server model id
  `qwen3.8-flash-next-ista-iq3_s`); the runner still addresses it as `local-only`, and the
  results folder keeps the original name so the two samples sit together
- script: `/tmp/series_iq3s_rep2.sh`, started 03:13 HKT once the context probe finished and
  `local-only` pointed at the model
- output: `chains_{en,ru,zh}_20k_64k_rep2.json`, `..._64k_rep2_8tasks.json`,
  `programs_v4_64k_rep2.json` — the first sample is never overwritten
- the Q4_K_XL programs run at 64k is deferred behind this one, as the owner asked

### Result of the IQ3_S replicate

Two full samples, 32k and 64k budgets (the budget is only a cutoff, so they are comparable):
Chains scored **49/75 in both**; programs 11/20 vs 12/20, so the averaged row reads 11.5/20.

Task-level agreement is the useful number: **86 of 95 tasks gave the same verdict**, and 9
flipped — en 7 and 13 swapped, zh 7 and 14 swapped, five programs changed. So the score is
stable at the set level and noisy at the task level, at roughly one task in ten.

### Q6_K_XL: two rows, on purpose

The rerun was first launched with sampling 0.3 and penalties 0.2 — a different mode from the
original run, which used the model's defaults. Instead of discarding the finished work, it
becomes a **separate row**:

- `*_64k.json` — second sample at 64k with model-default sampling, comparable to the first run;
- `*_64k_t03.json` — full run at 64k with 0.3 / 0.2, published as its own configuration.

Both are complete sets (chains en/ru/zh, the three subsets, programs), so the table shows two
rows for this model with different sampling rather than one averaged, misleading row.
