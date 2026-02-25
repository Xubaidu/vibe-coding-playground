#!/bin/bash
# Cron wrapper for stock tasks

cd "$(dirname "$0")"
# Load LARK_APP_ID, LARK_APP_SECRET from .env if present (e.g. for cron)
if [ -f .env ]; then set -a; source .env; set +a; fi
/usr/bin/python3 app.py heatmap

echo "[$(date)] Completed"
