# Stock Project

A tool to capture stock market heatmaps and send notifications via Lark (飞书).

## Features

- **Heatmap Capture**: Automatically capture 52ETF heatmap screenshots
- **Lark Notifications**: Send images and messages to Lark groups
- **Lark Bot**: WebSocket-based event listener for bot commands

## Project Structure

```
stock/
├── app.py                 # Main CLI entry point
├── run.sh                 # Cron wrapper script
├── requirements.txt       # Python dependencies
├── config/
│   ├── config.yaml        # Your configuration (git-ignored)
│   └── config.yaml.example
├── collectors/            # Data collection modules
│   └── etf_heatmap.py
├── notifiers/             # Notification channels
│   └── lark.py
├── bot/                   # Lark bot event handling
│   └── subscriber.py
├── tasks/                 # Scheduled tasks
│   └── daily_heatmap.py
└── tools/                 # Utilities
    └── query_chat.py
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install firefox
```

### 2. Configure Lark App

1. Go to [Lark Open Platform](https://open.feishu.cn/)
2. Create an app and get `app_id` and `app_secret`
3. Add permissions: `im:message`, `im:resource`, `im:chat:readonly`
4. Enable Bot capability
5. Add bot to your group
6. Get `chat_id` using: `python tools/query_chat.py`

### 3. Create config file and set Lark credentials

**Lark `app_id` and `app_secret`** — use env vars (recommended):

```bash
export LARK_APP_ID="your_app_id"
export LARK_APP_SECRET="your_app_secret"
```

**Config file** — for `chat_id` and other options:

```bash
cp config/config.yaml.example config/config.yaml
# Edit config/config.yaml: set lark.chat_id (and optional collectors)
```

For **cron**: `run.sh` loads `stock/.env` if present. Create `stock/.env` with `LARK_APP_ID=...` and `LARK_APP_SECRET=...` (and add `.env` to `.gitignore`). Alternatively export them in the crontab line.

## Usage

```bash
# Capture heatmap and send to Lark
python app.py heatmap

# Start Lark bot listener (WebSocket)
python app.py bot

# Show help
python app.py --help
```

## Cron Setup

```bash
# Edit crontab
crontab -e

# Add (example: weekdays 9:30 AM and 3:30 PM)
30 9 * * 1-5 /path/to/stock/run.sh >> /tmp/stock.log 2>&1
30 15 * * 1-5 /path/to/stock/run.sh >> /tmp/stock.log 2>&1
```

## License

MIT
