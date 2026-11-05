#!/bin/sh
# Safe health probe: refuses to run while a test series is active, because a
# second parallel request is what produced HTTP 503 on the 27B model.
cd "$(dirname "$0")/.." || exit 1
if pgrep -f "run_series_(q8|model)" >/dev/null 2>&1; then
  echo "skip: a test series is running, a parallel request can break it"
  exit 0
fi
API="${CHAIN_BENCH_ENDPOINT:-$(cat config/endpoint 2>/dev/null || echo http://127.0.0.1:21434)}"
curl -s -o /dev/null -w 'probe: HTTP %{http_code}\n' --max-time 120 \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-only","max_tokens":8,"messages":[{"role":"user","content":"ok"}]}' \
  "$API/v1/chat/completions"
