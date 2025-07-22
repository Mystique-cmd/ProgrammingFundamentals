#!/bin/bash

#== CONFIGURATION ==
LOG_DIR="/var/log"
LOG_NAME="sys.log"
MAX_AGE_DAYS=7
DATE_FORMAT="+%Y-%m-%d_%H:%M:%S"
ARCHIVE_NAME="${LOG_NAME}.$(date"$DATE_FORMAT"}.gz"

#==ROTATION ==
cd "$LOG_DIR" || exit 1
# Check if the log file exists
if [ -f "$LOG_NAME" ]; then
    echo "[*]Archiving log file: $LOG_NAME -> $ARCHIVE_NAME"
    cp "$LOG_NAME" "$ARCHIVE_NAME"
    gzip "$ARCHIVE_NAME"
    >$LOG_NAME  # Clear the original log file
else
    echo "[!]Log file $LOG_NAME does not exist."
fi
#== CLEANUP OLD LOGS ==
echo "[*]Cleaning up old logs older than $MAX_AGE_DAYS days"
find "$LOG_DIR" -name "${LOG_NAME}.*.gz" -mtime +$MAX_AGE_DAYS -exec rm -v {} \;
 echo "[✓] Log rotation completed.