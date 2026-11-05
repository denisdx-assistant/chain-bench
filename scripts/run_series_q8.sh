#!/bin/sh
# Full test series for Qwen3.8-27B-UD-Q8_K_XL on the local-only route.
# Sequential on purpose: the local endpoint serves one heavy model at a time.
# Resume-safe: a run whose result file exists is skipped.
set -u
cd /home/clawvm/.openclaw/workspace/chain-bench || exit 1

MODEL="Qwen3.8-27B-UD-Q8_K_XL"
OUT="results/$MODEL"
mkdir -p "$OUT"

COMMON="--model local-only --max-tokens 16000 --timeout 2400 --temp -1 --fp 0 --pp 0"

run_chains() { # $1=outfile $2=dataset $3=label
  f="$OUT/$1"
  if [ -f "$f" ]; then echo "skip $1 (exists)"; return 0; fi
  echo "=== $(date '+%H:%M') start $1 ($3)"
  python3 -u scripts/run_chains_guarded.py --dataset "$2" $COMMON --out "$f" \
      > "${f%.json}.log" 2>&1
  echo "=== $(date '+%H:%M') done  $1 -> $(tail -1 "${f%.json}.log")"
}

run_programs() {
  f="$OUT/programs_v4_16k.json"
  if [ -f "$f" ]; then echo "skip programs (exists)"; return 0; fi
  echo "=== $(date '+%H:%M') start programs_v4_16k"
  python3 -u scripts/run_frozen_guarded.py --dir datasets/programs/v4 $COMMON --out "$f" \
      > "${f%.json}.log" 2>&1
  echo "=== $(date '+%H:%M') done  programs -> $(tail -1 "${f%.json}.log")"
}

# 1. Test 1, full 17 tasks, three languages
run_chains chains_ru_20k_16k.json datasets/chains/ru/dataset_20k_17tasks.json "full 17, ru"
run_chains chains_en_20k_16k.json datasets/chains/en/dataset_20k_17tasks.json "full 17, en"
run_chains chains_zh_20k_16k.json datasets/chains/zh/dataset_20k_17tasks.json "full 17, zh"

# 2. Test 1, 8-task subset, three languages (continuity with the Q6 numbers)
run_chains chains_ru_20k_16k_8tasks.json datasets/chains/ru/dataset_20k_8tasks.json "subset 8, ru"
run_chains chains_en_20k_16k_8tasks.json datasets/chains/en/dataset_20k_8tasks.json "subset 8, en"
run_chains chains_zh_20k_16k_8tasks.json datasets/chains/zh/dataset_20k_8tasks.json "subset 8, zh"

# 3. Test 2, 20 frozen programs
run_programs

echo "=== $(date '+%H:%M') SERIES COMPLETE"
