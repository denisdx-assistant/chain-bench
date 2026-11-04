# chain-bench

**A private benchmark for local language models: multi-hop chains and code execution under noise**

---

## Abstract

Public benchmarks are prone to contamination: models may have seen their tasks during training. We describe a small private suite that measures not knowledge but the ability to **hold dependencies together**: multi-hop chains embedded in noise, and mental execution of a program whose comments and strings contain decoy code. Ground truth is computed by code or by running the program, never by hand. The suite is calibrated so that a weak model fails roughly half the time; otherwise the test saturates and stops discriminating between models.

Calibration was performed on Qwen3.8-27B (quant Q6) on 2×V100. Results: Test 1 — **41% errors** when questions are asked one at a time and **76%** when all questions are sent in a single request; Test 2 — **12%** at moderate difficulty and **60%** at the final difficulty level. The error profile is stable: the model solves arithmetic chains but fails when it has to combine two rules or attributes.

## 1. Introduction

Local model comparisons usually rely on public benchmarks. This has two problems: contamination and irrelevance. What matters for agentic work is not how much a model knows, but whether it can follow a chain of ten dependencies and tell code from text.

Requirements for the suite:

1. Answers are checked unambiguously — a single integer or an array.
2. Ground truth is computed programmatically.
3. Tasks are private: the exact texts do not appear in training corpora.
4. Difficulty is adjustable so that the target model fails about 50% of the time.

## 2. Test design

### 2.1 Test 1 — multi-hop chains

Seventeen tasks, one move type each: linear sums of offsets, group rules based on divisibility, star-shaped min/max, branching, age with aliases, sequential percentages, mass and colour thresholds, car attributes, counting by two features, ratios, rule priority, group versus group, ability and size, derived properties, a money trap, variable state mutation, and cancellation by order of mention.

Each task is surrounded by noise of the same type: identical predicates applied to other entities, near-duplicate identifiers, group rules about other classes. Entity names from the tasks never appear in the noise; this is checked automatically.

### 2.2 Test 2 — program execution

A small Python program over an array of ten integers: swaps, `+=`, `-=`, `*=`, slice sorting, reversal, conditionals, loops, recursion, regular expressions, type coercion with `str(a) + str(b)`, and aliasing (`arr2 = arr`). Noise consists of comments and string constants that contain **code which is never executed**. The model must mentally execute the program and report the final array and its sum. Ground truth is obtained by running the program.

## 3. Experimental setup

| Parameter | Value |
|---|---|
Hardware | 2× NVIDIA V100 |
Calibration model | Qwen3.8-27B, quant Q6 |
Orchestrator | aidir, OpenAI-compatible endpoint |
`max_tokens` | 16000 |
Temperature | default |

The 16000 budget was chosen experimentally for Q6: at 700 and 3000 tokens the reasoning consumes the whole allowance and the response comes back empty (`finish=length`). Empty responses are treated as a harness artefact and counted separately from wrong answers.

**Budget is not the lever; loop control is.** Qwen3.8-27B Q6 works at 16000. Flash-Next first looked like it needed 48–65k: calls stopped with `finish=length`. Inspection showed those long generations were degenerate repetition — the model looped over the same noise block. With `frequency_penalty` and `presence_penalty` at 0.3, temperature 0.3, and a streaming repetition guard (abort when an 8-word shingle repeats more than 40 times), 32000 tokens is sufficient. Raising the cap blindly does not help: a loop consumes any budget.

## 4. Results

### 4.1 Test 1

| Mode | Correct | Errors | Time |
|---|---|---|---|
One question per request | 10/17 | **41%** | ~17 min |
All 17 in one request | 4/17 | **76%** | 90 s |

### 4.2 Test 2

| Configuration | Conditions | Correct | Errors |
|---|---|---|---|
v1 heavy | ops=15, comments=800, extras=300, traps=80 | 7/8 | 12% |
v2 control flow | ops=12, comments=600, extras=200, traps=60 | 7/8 | 12% |
v3 nested | ops=25, comments=1500, extras=500, traps=120 | 7/8 | 12% |
v4 final | ops=20, comments=7400, extras=800, traps=150, ~106k tokens, array+sum | 2/5 | **60%** |

On a simple set of 24 tasks without noise both models scored 24/24 — a ceiling that does not discriminate.

## 5. Error analysis

In Test 1 the failures were tasks 2, 7, 9, 13, 14, 15 and 17 — all requiring combination of rules or attributes. Pure arithmetic chains (1, 3, 4, 6, 8, 10, 11, 12, 16) were solved completely.

In Test 2 the final configuration produced two distinct failure modes: a near miss (one element off by two, sum 332 instead of 330) and large deviations where an entire branch of operations was lost.

## 6. Discussion

1. **One task per request is markedly better.** The batched mode is about eleven times faster but twice as error-prone. For real work this argues for narrow requests.
2. **`reasoning_effort` does not help.** The parameter changes the length of reasoning (12,088 → 14,919 characters) but not correctness.
3. **Budget is part of the method.** A small `max_tokens` turns the test into a limit check rather than a capability check.
4. **Structural complexity beats volume.** Adding comments up to 65–100k tokens did not raise the error rate; recursion, regex, type coercion and aliasing did.

## 7. Limitations

- Few tasks: 17 chains and 5 programs — the statistics are weak, conclusions concern error profiles rather than exact rates.
- One hardware configuration and one model at the calibration stage.
- Language variants currently cover eight representative chain tasks.

## 8. Reproducibility

```bash
# tasks and ground truth
python3 scripts/build_tasks.py

# chain dataset with noise
python3 scripts/gen_noise.py --seed 21 --tokens 20000 --noise 300 --out dataset_20k

# test 1: one by one and batched
python3 scripts/run_chains.py --dataset dataset_20k.json --model local-only
python3 scripts/run_batch.py  --dataset dataset_20k.json --model local-only

# test 2: programs
python3 scripts/run_programs_v4.py --model local-only --n 5 --comments 7400 --extras 800 --traps 150
```

All generators are deterministic by seed: identical parameters produce byte-identical data.

## Appendix A. Task types

| # | Move type | Answer |
|---|---|---|
1 | linear chain, sum of offsets | 13 |
2 | group rules by divisibility | 6 |
3 | star, max minus min | 40 |
4 | branching, two paths | 6 |
5 | age and alias | 2 |
6 | sequential percentages | 1760 |
7 | mass + colour thresholds | 5 |
8 | mileage + colour + divisibility | 40 |
9 | counting by two features | 2 |
10 | ratio instead of difference | 3 |
11 | rule priority | 14 |
12 | group versus group | 100 |
13 | ability and size, signed difference | -5 |
14 | derived property | 5 |
15 | money trap | 120 |
16 | variable state mutation | 39 |
17 | cancellation by order of mention | 110 |

## Appendix B. Repository layout

```
scripts/    generators for tasks, noise and programs; runners
tasks/      tasks and ground truth (md + json)
datasets/   chains/ — noisy documents; programs/ — programs with expected outputs
results/    run results (json)
protocol.md test log: setup, rules, observations
```

## License

Code — MIT. Texts and datasets — CC BY 4.0.
