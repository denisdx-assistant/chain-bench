# Methodology

This document describes the harness as an artifact: what is measured, how a
run is executed, and which rules make results comparable across models.

## 1. Purpose

The benchmark targets a specific failure mode of local models used inside
agent loops: a long noise-heavy context, a small multi-hop task, and a single
exact answer. Success requires the model to locate the relevant statements in
noise, chain them, and return one integer (or one program result) without
paraphrasing. Accuracy and wall-clock latency are both recorded; degenerate
behaviour (loops, length cuts) is recorded separately from ordinary wrong
answers.

## 2. Test 1 — arithmetic chains in noise

- A document of approximately 20k tokens of synthetic noise (300 lines) is
  generated from the same generator for every language, so that the noise is
  semantically neutral and the only difference between language variants is
  the language itself, including the task text.
- The document contains statement chains (A is higher than B by N metres, B is
  higher than C by M metres, ...) and a question asking for a derived value.
- 17 tasks cover sums of offsets, divisibility rules, mass/colour attributes,
  counting by two features, discounts, array sums and cancellation by order of
  mention.
- Ground truth is computed by code, never by hand.
- The answer must be a single integer.

## 3. Test 2 — frozen programs

- 20 Python programs (seeds 300–319) build a 10-element array with decoy code
  in comments and strings, nested control flow and arithmetic over 20
  operations.
- The model receives the program and must return the final array and its sum
  in a fixed format (`ARRAY: [...]`, `SUM: n`).
- Both the array (element by element) and the sum must match. No partial
  credit.
- The set is frozen so that every model sees byte-identical input.

## 4. Harness

### 4.1 Loop guard

Requests are streamed. The harness counts 8-word shingles over the accumulated
content and reasoning, and closes the connection when any shingle appears more
than 40 times. The task is then marked `kind=loop` instead of silently
consuming the whole budget. This turns a rare degenerate case into a
measurable category.

### 4.2 Sampling controls

Guarded runs use temperature 0.3 and `frequency_penalty` / `presence_penalty`
of 0.3. These values were chosen because they suppress the repetition
observed on hard tasks; they are part of the run configuration and are
recorded with every series. Runs before the guard was introduced used default
sampling and are labelled as such.

### 4.3 Budget

The budget is a first-class parameter, not a detail.

- Too small a budget turns a capable model into an empty answer: reasoning
  alone can exceed it, and the response ends with `finish_reason=length`.
- A budget that is too large does not help a loop: a loop consumes any budget.
- Working value for 27B-class models: 16k. Working value for
  Flash-Next-class models with the guard: 32k.

### 4.4 Retry policy for length cuts

A response that stops on the length cap **without** repetition is a genuine
under-budget case, not a loop. Such items are re-run separately at four times
the budget (131072) with the guard still on. The retry is reported next to the
original, and the original is never silently replaced. `kind=loop` items are
not retried with a bigger budget: the cap is not the cause there.

### 4.5 Provenance

Every result file records the model it was produced on. Guarded runners query
the router (`/v1/models/local-only`) before the run and store
`resolved_provider` and `resolved_model` in the result JSON. Series filenames
encode the test, language and budget. Result folders are named exactly after
the model.

### 4.6 Invalid runs

Batch runs that ask one request to answer all tasks at once are kept for the
record but excluded from tables: parsing, not the model, decides the score.
They live in `results/_invalid/`.

### 4.7 Scoring is validated, not assumed

Two guards protect against a silently wrong verdict:

- The runner reads the expected answer from `expected_array`/`expected_sum` (or
  the legacy `array`/`sum`) and **stops with a schema error** if neither is
  present, instead of scoring every answer wrong.
- `scripts/selftest_scoring.py` checks the scoring function on exact answers,
  alternative wording, altered array, altered sum, empty and truncated answers,
  the legacy schema, and a missing schema. It runs in under a second and is the
  first thing to run before a series.
- `scripts/rescore.py` re-parses saved raw answers and reports any row whose
  verdict would change. Since every row keeps the raw answer, a scoring bug can
  be corrected afterwards without re-running the model.

## 5. Scoring

- Correct — exact match. Programs require both array and sum.
- Errors — 100% minus the share of exact matches.
- Median latency — wall-clock seconds per task, including queue time. It is
  not pure inference time and must not be compared against vendor throughput
  figures.
- Median reasoning — median character count of `reasoning_content`,
  comparable only within the same task set.
- Loops and length cuts — separate counters, never folded into "errors".

## 6. Error profile (test 1, 17 tasks, Q6 at 16k)

Failures: tasks 2, 7, 9, 13, 14, 15, 17. All of them require combining two
rules or selecting one of several attributes: divisibility (2), mass + colour
(7), counting by two features (9), ability + size (13), a derived property
(14), a money trap (15), cancellation by order of mention (17).

Clean passes: tasks 1, 3, 4, 6, 8, 10, 11, 12, 16 — plain arithmetic chains,
including long ones.

Conclusion: the model sums offsets along a chain reliably but loses rules when
two of them must be selected or combined. This is precisely the skill an agent
loop needs.

## 7. Pitfalls

1. **An empty answer is not a wrong answer.** They are counted separately.
2. **Routing is a trap.** Set the exact model id, not a smart route; record the
   resolved id with every run, because the target of `local-only` changes.
3. **Prefix cache.** Re-sending the same document yields ~99.9% cached tokens
   and sub-second responses; a series over one document barely loads prefill,
   so latency numbers are not pure inference.
4. **Concurrency.** The 27B model reports `max_concurrent_requests: 2`; a third
   request waits, which inflates latencies.
5. **Reasoning effort** changes reasoning length only marginally and does not
   change correctness; it is not a useful lever.
6. **Language** has a small effect on test 1; the trilingual subset was run to
   bound it, not to prove a trend.

7. **Concurrency is a hard limit.** The 27B model cannot serve two requests at
   once on this host: a parallel probe returns HTTP 503 and can break an active
   series. The harness is strictly sequential and `scripts/probe.sh` refuses to
   run while a series is active. Do not health-check the endpoint by hand during
   a run.

## 8. Open questions

- Whether the language of a document shifts accuracy on rule-combination
  tasks, beyond the 8-task subset measured so far.
- Whether the four quantisations in preparation reproduce the Q6 profile or
  degrade differently.
- How stable the calibrated difficulty is across restarts and cache states.
