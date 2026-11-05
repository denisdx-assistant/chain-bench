# Calibration

How the suite was tuned to a useful difficulty, and what "automatic adjustment"
means here.

## Goal

A benchmark that a strong model solves completely does not discriminate, and
one that no model solves is noise. The target is a reference model that fails
roughly **half** the tasks: at that point a difference of a few points is
meaningful, and the test still leaves room for a better model.

Reference model for calibration: **Qwen3.8-27B-UD-Q6_K_XL**.

## What was varied

Only two levers were used to raise difficulty, in this order.

1. **Structural complexity.** More operations, nested control flow, recursion,
   regular expressions, type coercion, aliasing, and two-rule tasks that require
   selecting or combining predicates. This moved accuracy the most.
2. **Noise volume.** The same document type, longer: 20k, 40k and 60k tokens of
   semantically neutral statements, near-duplicate identifiers and rules about
   other classes.

Deliberately **not** used as a difficulty lever: a small token budget. A budget
that is too small produces empty answers, which measure the harness, not the
model.

## Steps (all on the reference model)

| Step | Configuration | Result | Decision |
|---|---|---|---|
| Clean tasks, no noise | 24 tasks | 24/24 | ceiling: no discrimination |
| Budget probe | max_tokens 700 and 3000 | nearly all answers empty | budget too small, raise it |
| Budget 6000 | 17 tasks, 20k noise | 6/6 answered, one quality error | still tight, move to 16k |
| Budget 16000 | 17 tasks, 20k noise, 300 lines | **10/17, 41% errors** | accepted as the chain set |
| Noise sweep | 20k / 40k / 60k tokens | 6/6 at every level | noise volume is not the lever |
| Programs, easy | 8 ops, light noise | 8/8 | too easy |
| Programs, heavy | 15 ops, comments and traps | 7/8 | still easy |
| Programs, control flow | 12 ops, branches and loops | 7/8 | still easy |
| Programs, nested | 25 ops, deep nesting | 7/8 | still easy |
| Programs, v4 | 20 ops, ~106k tokens of comments and decoys, array + sum | **2/5 and 11/20** | accepted for test 2 |

Chain set landed at 41% errors, program set at 45% — close enough to the 50%
target to discriminate without saturating.

## Calibration of the harness itself

- **One task per request** is the scoring mode. A batch run with all 17 tasks in
  one request scored 4/17 (76% errors) and about eleven times faster; it
  measures parsing and instruction-following under load, not the target skill,
  so it is kept in `results/_invalid/` and excluded from tables.
- **Retries.** An empty answer caused by the length cap is a harness artefact.
  Such items are re-run at four times the budget and reported separately; they
  are never silently counted as model errors.
- **Loop guard.** Long generations on hard tasks turned out to be degenerate
  repetition in some cases. A streaming guard aborts a response when one 8-word
  window repeats more than 40 times and marks it `kind=loop`, so a loop becomes
  a measurable category instead of a timeout.

## Adjusting for another model

No per-model retuning is done. Every model sees the frozen datasets byte for
byte, with a documented budget and sampling configuration recorded in
`results/run-configs.json`. If a model is much weaker or much stronger, that is
the result, not a reason to change the test.

The only exception is budget: a model whose reasoning is longer than the
reference needs a budget large enough to answer at all. The rule used here is
16k for 27B-class models and 32k for Flash-Next-class models with the guard
enabled.
