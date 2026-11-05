#!/bin/sh
# While the Q8 series runs, refresh the generated tables and push when they change.
cd "$(dirname "$0")/.." || exit 1
while pgrep -f "run_series_q8.sh|run_series_model.sh|resume_q8_when_ready.sh|queue_watch.sh" >/dev/null 2>&1; do
  if python3 scripts/sync_readme.py | grep -q updated; then
    git add -A
    git commit -q -m "data: refresh result tables during Q8 series ($(date '+%H:%M'))"
    GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=20' git push -q origin main && \
      echo "$(date '+%H:%M') pushed"
  fi
  sleep 900
done
echo "$(date '+%H:%M') series finished, autopush stopped"
