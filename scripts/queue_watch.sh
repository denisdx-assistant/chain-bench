#!/bin/sh
# Run the full series for a queued model as soon as the local route serves it.
# Refuses to run while another series is active; matches by model name only.
cd /home/clawvm/.openclaw/workspace/chain-bench || exit 1
API="http://192.168.1.111:21434"
for i in $(seq 1 288); do
  if pgrep -f "run_series_(q8|model)" >/dev/null 2>&1; then sleep 180; continue; fi
  loaded=$(curl -s --max-time 10 "$API/v1/models/local-only" | python3 -c "
import sys,json
a=(json.load(sys.stdin).get('aidir') or {})
print((a.get('resolved_model') or '').lower())" 2>/dev/null)
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
    echo "$(date '+%H:%M') $model is served, starting series"
    sh scripts/run_series_model.sh "$model" "$prof" >> "results/$model/series.log" 2>&1
    python3 - "$model" <<'PY'
import json,sys
p='results/queue.json'; q=json.load(open(p))
for e in q['queue']:
    if e['model']==sys.argv[1]: e['status']='done'
json.dump(q, open(p,'w'), indent=1, ensure_ascii=False)
PY
    echo "$(date '+%H:%M') $model series finished"
  fi
  sleep 300
done
