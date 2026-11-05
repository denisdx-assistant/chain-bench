#!/bin/sh
# Full test series for one model folder. Usage: run_series_model.sh <folder> <profile>
# profile: 27b (16k, default sampling) | flash-next (32k, temp 0.3, penalties 0.3)
set -u
cd "$(dirname "$0")/.." || exit 1
MODEL="$1"; PROFILE="${2:-27b}"
OUT="results/$MODEL"
mkdir -p "$OUT"
case "$PROFILE" in
  27b-32)        COMMON="--model local-only --max-tokens 32000 --timeout 3600 --temp -1 --fp 0 --pp 0" ;;
  flash-next)    COMMON="--model local-only --max-tokens 32000 --timeout 2400 --temp 0.3 --fp 0.3 --pp 0.3" ;;
  flash-next-02) COMMON="--model local-only --max-tokens 32000 --timeout 2400 --temp -1 --fp 0.2 --pp 0.2" ;;
  *)          COMMON="--model local-only --max-tokens 16000 --timeout 2400 --temp -1 --fp 0 --pp 0" ;;
esac

run_chains() {
  f="$OUT/$1"
  if [ -f "$f" ]; then echo "skip $1"; return 0; fi
  echo "=== $(date '+%H:%M') start $1 ($3)"
  python3 -u scripts/run_chains_guarded.py --dataset "$2" $COMMON --out "$f" > "${f%.json}.log" 2>&1
  echo "=== $(date '+%H:%M') done  $1 -> $(tail -1 "${f%.json}.log")"
}
run_programs() {
  f="$OUT/programs_v4_16k.json"
  if [ -f "$f" ]; then echo "skip programs"; return 0; fi
  echo "=== $(date '+%H:%M') start programs"
  python3 -u scripts/run_frozen_guarded.py --dir datasets/programs/v4 $COMMON --out "$f" > "${f%.json}.log" 2>&1
  echo "=== $(date '+%H:%M') done  programs -> $(tail -1 "${f%.json}.log")"
}

run_chains chains_ru_20k_16k.json datasets/chains/ru/dataset_20k_17tasks.json "full 17 ru"
run_chains chains_en_20k_16k.json datasets/chains/en/dataset_20k_17tasks.json "full 17 en"
run_chains chains_zh_20k_16k.json datasets/chains/zh/dataset_20k_17tasks.json "full 17 zh"
run_chains chains_ru_20k_16k_8tasks.json datasets/chains/ru/dataset_20k_8tasks.json "subset 8 ru"
run_chains chains_en_20k_16k_8tasks.json datasets/chains/en/dataset_20k_8tasks.json "subset 8 en"
run_chains chains_zh_20k_16k_8tasks.json datasets/chains/zh/dataset_20k_8tasks.json "subset 8 zh"
run_programs
echo "=== $(date '+%H:%M') SERIES COMPLETE $MODEL"
