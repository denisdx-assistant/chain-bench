# Pending runs

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
