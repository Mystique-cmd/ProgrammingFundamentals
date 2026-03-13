#! /usr/bin/bash

WATCHLIST="watchlist.txt"
LOGDIR="logs"
mkdir -p $LOGDIR

echo "[+] Starting Tracewatch..."
while read -r path; do
    echo "[*] Monitoring $path"
    inotifywait -m -e access,modify,delete "$path"
    while read -r file event; do
        timestamp=$(date '%Y-%m-%d %H:%M:%S')
        echo "$timestamp | $event | $file" >> "$LOGDIR/tracewatch.log"
    done &
done < "$WATCHLIST"
wait