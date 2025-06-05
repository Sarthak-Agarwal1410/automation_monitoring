#!/bin/bash

LOGFILE="$1"
PATTERN="$2"
THRESHOLD="$3"
WINDOW="$4"  # in seconds

if [[ -z "$LOGFILE" || -z "$PATTERN" || -z "$THRESHOLD" || -z "$WINDOW" ]]; then
  echo "Usage: $0 /path/to/logfile \"PATTERN\" threshold time_window"
  exit 1
fi

declare -a timestamps=()

function cleanup_old_entries {
  local now=$(date +%s)
  local new_timestamps=()
  for ts in "${timestamps[@]}"; do
    if (( now - ts <= WINDOW )); then
      new_timestamps+=("$ts")
    fi
  done
  timestamps=("${new_timestamps[@]}")
}

function handle_line {
  local line="$1"
  if echo "$line" | grep -E "$PATTERN" >/dev/null; then
    timestamps+=($(date +%s))
    cleanup_old_entries
    if (( ${#timestamps[@]} >= THRESHOLD )); then
      echo "[ALERT] Pattern '$PATTERN' occurred ${#timestamps[@]} times in the last $WINDOW seconds!"
      # Reset to prevent repeated alerting
      timestamps=()
    fi
  fi
}

# Monitoring loop
echo "Monitoring '$LOGFILE' for pattern: '$PATTERN'..."

tail -Fn0 "$LOGFILE" 2>/dev/null | while read -r line; do
  handle_line "$line"
done
