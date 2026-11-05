#!/bin/sh
# Run the full series for a queued model as soon as the local route serves it.
# Refuses to run while another series is active; matches by model name only.
cd "$(dirname "$0")/.." || exit 1
API="${CHAIN_BENCH_ENDPOINT:-$(cat config/endpoint 2>/dev/null || echo http://127.0.0.1:21434)}"
for i in $(seq 1 288); do
  if pgrep -f "run_series_(q8|model)" >/dev/null 2>&1; then sleep 180; continue; fi
  loaded=$(curl -s --max-time 10 "$API/v1/models/local-only" | python3 -c "
import sys,json
a=(json.load(sys.stdin).get('aidir') or {})
print(((a.get('resolved_provider') or '') + ' ' + (a.get('resolved_model') or '')).lower())" 2>/dev/null)
  [ -z "$loaded" ] && { sleep 300; continue; }
  todo=$(python3 - "$loaded" <<'PY'
import json,sys
loaded=sys.argv[1]
q=json.load(open('results/queue.json'))
for e in q['queue']:
    if e['status']!='pending': continue
    name=e['model'].lower()
    if name in loaded or loaded in name:
        print(e['model'], e['profile']); break
PY
)
  if [ -n "$todo" ]; then
    model=$(echo "$todo" | cut -d' ' -f1); prof=$(echo "$todo" | cut -d' ' -f2)
    echo "$(date '+%H:%M') $model is served, waiting until it answers"
    ready=0
    for w in $(seq 1 30); do
      code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 180 \
        -H 'Content-Type: application/json' \
        -d '{"model":"local-only","max_tokens":4,"messages":[{"role":"user","content":"ok"}]}' \
        "$API/v1/chat/completions")
      if [ "$code" = "200" ]; then ready=1; break; fi
      echo "$(date '+%H:%M') not ready yet (HTTP $code), waiting"
      sleep 60
    done
    if [ "$ready" != "1" ]; then echo "$(date '+%H:%M') $model did not answer in 30 min, back to queue"; sleep 300; continue; fi
    echo "$(date '+%H:%M') $model answers, starting series"
    mkdir -p "results/$model"
    sh scripts/run_series_model.sh "$model" "$prof" >> "results/$model/series.log" 2>&1
    python3 - "$model" <<'PY'
import json,sys,glob,os
model=sys.argv[1]
produced=bool([f for f in glob.glob(os.path.join('results',model,'*.json')) if '.failed.' not in f])
p='results/queue.json'; q=json.load(open(p))
for e in q['queue']:
    if e['model']==model and produced: e['status']='done'
json.dump(q, open(p,'w'), indent=1, ensure_ascii=False)
print('done' if produced else 'still pending: no result files')
PY
    echo "$(date '+%H:%M') $model series finished"
  fi
  sleep 300
done
