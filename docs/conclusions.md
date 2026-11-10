# What the numbers mean

This document is the long form of the "What it shows" paragraph in the README. It states what
the benchmark can and cannot support, with the figures behind each claim.

## 1. How noisy this system is

The sets are small: 17 chains per language and 20 programs. A one-task difference is not a
result.

Two independent measurements of the same model quantify the noise:

| Pair | Chains agreed | Task-level flips |
|---|---|---|
| IQ3_S, 32k vs 64k, 95 tasks | 49/75 in both | 9 tasks of 95 (~10%) |
| Q6_K_XL, 16k vs 64k, 95 tasks | 48/75 vs 47/75 | — |
| Q8_K_XL, 16k vs 32k | identical per language | — |

Set-level chain scores repeat to within one task of seventeen; individual chain tasks flip
about once in ten. Program scores are less stable — see section 2 — so a one- or two-program
difference is not evidence either.

**Why there is no confidence interval.** A proper interval needs either many repeats of the
same configuration or a homogeneous pool of tasks. We have neither: most models were run once
or twice, and the two tests measure different things (integer arithmetic in a long noisy
document; state tracking through Python-like code). Any interval computed from n=1 or n=2
would be an artefact of the assumption, not a measurement. What can be stated honestly is the
ordering, plus the size of the flip rate above.

**What would fix it:** three to five replicates per model, or a paired design that runs every
model on the same fixed task subset and reports win/loss counts. Until then, treat differences
of one or two tasks as ties.

## 2. Quantisation: the 27B ladder is flat

All three quantisations ran on the same host with the same tasks.

| Model | Chains (51) | Subsets (24) | Programs (20) |
|---|---|---|---|
| Q4_K_M (two runs averaged) | **34.5** | 12 | 12.5 |
| Q6_K_XL (two runs averaged) | 34 | 13 | 13 |
| Q8_K_XL (two runs averaged) | 32.5 | 13 | 15 |

The expected monotone ladder does not appear: Q4_K_M leads on chains, ties Q8 on programs and
is one behind on subsets. Every gap is one to three tasks, i.e. inside the flip rate.

**The Q4_K_M lead did not reproduce.** Its first run scored 35 chains and 15 programs; a
second full run at identical settings scored 34 and 10, so the average sits level with Q6 and
behind Q8 on programs. The first run's lead was a small-sample effect, exactly as the flip
rate predicted.

**Programs are the least reproducible part of the suite.** Between the two Q4_K_M runs 7 of 20
programs changed verdict (five lost, two gained), against one or two of 17 on the chains. A
program answer depends on tracing a long chain of state changes without a single slip, so a
small perturbation in sampling or in the runtime flips the result. The practical consequence:
a single program score is weak evidence, and comparing two models on programs needs several
runs per model. The second run also ran on a different runtime (two accelerators under NCCL),
which may add its own variance on top of sampling.

That is itself the useful finding: at this task difficulty, going from 8 bits to 4 bits does
not buy or cost quality, while it does move speed and memory.

## 3. The 1-bit coder build fails exactly where coding lives

| Set | IQ1_M |
|---|---|
| Chains (51) | 34 |
| Subsets (24) | 15 |
| Programs (20) | **0 of 8 finished**, 12 hit the budget |

On short-context chain tasks it sits mid-field, only two tasks behind Q4_K_M. On programs — a
142k-token prompt containing code that must be traced — it either ran out of budget (12 of 20
wrote exactly 64 000 tokens and stopped) or answered wrongly in every case that did finish.

Two caveats belong with this number. It is a coder build, not a quantisation of the same
family, and it **understands Russian but answers in English**, so its Russian chains measure
reasoning, not language.

## 4. Flash-Next vs the dense 27B: same quality, different speed

| | 27B Q4_K_M | Flash-Next IQ4_XS |
|---|---|---|
| Chains (51) | 35 | 35 |
| Programs (20) | 15 | 16.5 |
| Generation at ~20k | 23–26 t/s | 85–96 t/s |
| Prefill at 250k | 431 t/s (measured at 190k) | 2427 t/s |
| Generation at 250k | ~10 t/s (Q6) | 84 t/s |

On ordinary task-sized prompts the quality is the same and the speed is already three to four
times higher. On long context the gap becomes structural: the dense model's generation falls
to about ten tokens per second at a quarter-million tokens, while the MoE model keeps 84.

The same pattern holds for prefill: IQ4_XS 2427 t/s, Q4_K_XL 1836, IQ3_S 2538 at 250k, against
431–537 for the dense 27B. Since prefill dominates the wall time of a long-context request, and
a programmer's request is long by nature, this is the difference that matters in practice.

Batching follows the same logic and is not universal: with two concurrent clients Q6_K_XL
raised aggregate throughput from 242 to 343 token/s (+42%), while IQ1_M lost 8%. The benefit
appears when a single stream does not already saturate the hardware.

## 5. Programs discriminate, chains do not

On chains, six of the models sit between 32 and 35 correct out of 51 — a band narrower than the
noise. On programs the same models range from 0 to 18 out of 20.

| Model | Programs (20) |
|---|---|
| IQ4_XS | 16.5 |
| Q4_K_M | 15 |
| Q8_K_XL | 15 |
| Q4_K_XL | 15 |
| deepseek-v4.1-flash | 14 |
| Q6_K_XL | 13 |
| IQ3_S | 11.5 |
| IQ1_M | 0 |
| gemma-4-31B | 0 |

Programs are the closest thing here to real coding work: a long prompt, exact state tracking
through code, no tolerance for a single wrong swap. Chains mostly measure reading a long
document — necessary, but not sufficient. **If one number has to represent coding ability, it
is the program column.**

## 6. Budget is a cutoff, not a parameter of quality

The recording treats `finish=length` as unresolved, retries it at a larger budget, and only
then decides. Two examples show this is the right call:

- Q6_K_XL scored 48/75 chains at 16k and 47/75 at 64k — the budget moved nothing.
- IQ4_XS program `v4_seed313` wrote exactly 64 000 tokens and was cut; retried at 96k it
  finished in **17 496 tokens**, answered correctly, and took 381 s. The cut was hiding a
  correct answer, not a failure.

For that reason, tables average runs made at different budgets once the cut tasks are resolved,
and rows with unresolved tasks are marked.

## 7. What the failures look like

Most misses are wrong numbers with `finish=stop`, not refusals or format errors: the model
finished, committed to an answer, and the arithmetic was wrong. Empty replies are rare
(one chain in the whole corpus) and are treated as unresolved rather than as failures.

This matters for how to read the benchmark: it is not measuring whether the model can produce
the required shape of answer — all of them can — it is measuring whether the reasoning survives
a long noisy document.

## 8. Outliers and dropped models

- **gemma-4-31B-it-UD-Q8_K_XL**: fast (43 t/s) but the weakest quality — 30/51 chains and 0/20
  programs. Useful as a speed reference, not as a candidate.
- **deepseek-v4.1-flash** (hosted): English chains 12/17 and programs 14/20; the rest was never
  planned.
- **Ripple-65B-Preview-Q6_K**: dropped — too heavy for this hardware and too weak to be worth
  the hours.
- **Orca Q1**: dropped after a look; clearly weak, the existing run is reference enough.

## 9. Limits of this study

1. One hardware configuration, one local endpoint.
2. Tests are heterogeneous; no pooled statistic.
3. One or two repeats per model; no confidence intervals.
4. Latency medians include queue time.
5. Large-context speed figures come from a synthetic probe, not from tasks; they are an upper
   bound (see `docs/speed.md`).
6. Sampling matters less than expected: a full second row at `t 0.3 · pen 0.2` moved chains
   from 47 to 45 of 75 and programs not at all — within the same noise band.
