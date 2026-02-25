"""Load configuration from config.yaml and env vars"""

import os
import yaml
from pathlib import Path

_config_path = Path(__file__).parent / "config.yaml"

with open(_config_path, "r") as f:
    _config = yaml.safe_load(f)

LARK_APP_ID = os.environ.get("LARK_APP_ID")
LARK_APP_SECRET = os.environ.get("LARK_APP_SECRET")
LARK_CHAT_ID = _config["lark"]["chat_id"]

# Collectors config
COLLECTORS = _config.get("collectors", {})
