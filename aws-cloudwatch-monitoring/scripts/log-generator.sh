#!/bin/bash

LOG_FILE="/var/log/myapp/app.log"

while true
do
  echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') Request received from 10.0.0.$((RANDOM % 255))" >> $LOG_FILE

  if [ $((RANDOM % 5)) -eq 0 ]; then
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') DB connection failed - timeout after 30s" >> $LOG_FILE
  fi

  if [ $((RANDOM % 7)) -eq 0 ]; then
    echo "[WARN] $(date '+%Y-%m-%d %H:%M:%S') Slow response detected: $((RANDOM % 2000 + 800))ms" >> $LOG_FILE
  fi

  sleep 1
done