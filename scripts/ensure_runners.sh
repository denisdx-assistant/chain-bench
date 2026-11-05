#!/bin/sh
# Start any missing background helper. Safe to call repeatedly.
cd /home/clawvm/.openclaw/workspace/chain-bench || exit 1
started=""
pgrep -f queue_watch.sh >/dev/null 2>&1 || { nohup sh scripts/queue_watch.sh > results/queue_watch.log 2>&1 & started="$started queue_watch"; }
pgrep -f autopush_series.sh >/dev/null 2>&1 || { nohup sh scripts/autopush_series.sh > results/autopush.log 2>&1 & started="$started autopush"; }
[ -n "$started" ] && echo "started:$started" || echo "ok"
