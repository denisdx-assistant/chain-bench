#!/bin/sh
# Wait until the Q8 model is schedulable again, then resume its series.
# Refuses to start on any other provider: results must not be filed under Q8
# if a different model is loaded on the shared local route.
cd "$(dirname "$0")/.." || exit 1
WANT="local_Qwen3.8-27B-UD-Q8_K_XL"
API="${CHAIN_BENCH_ENDPOINT:-$(cat config/endpoint 2>/dev/null || echo http://127.0.0.1:21434)}"

for i in $(seq 1 288); do   # up to 24 hours at 5-minute steps
  prov=$(curl -s --max-time 10 "$API/v1/models/local-only" \
         | python3 -c "import sys,json;print((json.load(sys.stdin).get('aidir') or {}).get('resolved_provider') or '')" 2>/dev/null)
  if [ "$prov" = "$WANT" ]; then
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 120 \
      -H 'Content-Type: application/json' \
      -d '{"model":"local-only","max_tokens":8,"messages":[{"role":"user","content":"ok"}]}' \
      "$API/v1/chat/completions")
    if [ "$code" = "200" ]; then
      echo "$(date '+%H:%M') $WANT is ready, resuming series"
      sh scripts/run_series_q8.sh >> results/Qwen3.8-27B-UD-Q8_K_XL/series.log 2>&1
      echo "$(date '+%H:%M') series finished"
      exit 0
    fi
    echo "$(date '+%H:%M') provider matches but request returned $code, waiting"
  fi
  sleep 300
done
echo "$(date '+%H:%M') gave up waiting for $WANT"
