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

## Sharing the model with OpenClaw

The benchmark talks to the same single-slot server that OpenClaw agents use, and
one request at a time is admitted. A chain task holds that slot for minutes, so
before each request the runner checks the server queue and, if other clients are
already waiting, sleeps in one-minute steps for up to fifteen minutes. Requests
also identify themselves as `chain-bench`, so a task list on the server shows who
sent what. Set `CHAIN_BENCH_POLITE=0` to disable the yielding for an unattended run.

## Pause and resume

A long series can be stopped without losing work. Both runners append each finished
task to the result file as soon as it lands, and both accept `--resume`, which reads
the existing file and skips the tasks already there. A task that ended with
`finish=length`, or with a transport error, is retried rather than skipped.

To stop between tasks, create a file named `PAUSE` in the repository root (or point
`CHAIN_BENCH_PAUSE_FILE` at another path). The runner finishes the task in flight and
exits; nothing already recorded is lost. Remove the file and rerun the same command
with `--resume` to continue.

`--dry-run` lists the tasks that would run, without contacting the model:

```
python3 scripts/run_frozen_guarded.py --dir datasets/programs/v4 --out results/<model>/programs_v4_16k.json --resume --dry-run
```

## Hardware note on the 27B Q4_K_M row

`Qwen3.8-27B-UD-Q4_K_M` was served on a **single** GPU with a configuration tuned
for a 3090. That is why its series takes 442 minutes while Q8, running on two
cards, finishes the same sets in 147. The label in the summary table carries the
same note, so the comparison is not read as a property of the quantisation.

## Tasks that reference entities missing from the document

Two tasks ask about entities the document never lists: chain 11 (ship-15 vs
ship-18) and chain 12 (heron-09, цапля-09). This is deliberate — both are
determined by rules, not by records:

- ships: capacity comes from divisibility rules (by five `+10 t`, by three
  `-4 t`, by seven `-4 t`; when two rules match, only the rule of five applies),
  so 15 → base+10 and 18 → base−4, a difference of 14;
- herons: "all jays are 30 g heavier than all crows" and "all crows are 20 g
  heavier than all herons" give 150 → 120 → 100.

The check is whether a model applies the rules instead of searching the text for
a record. The outcome splits sharply by language: Russian runs solve chain 11 in
5 of 5 cases and chain 12 in 6 of 7, while English runs solve 11 in 0 of 7 and 12
in 1 of 7. So the task is solvable and is a clean discriminator, not a defect.
A run that stops at "the entity is not in the document" and then re-reads the
text until the budget ends is a genuine capability failure.
