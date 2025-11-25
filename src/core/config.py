"""config.py is for configuring application
APP_NAME = "QTPaint"
APP_VERSION = "1.0.0"
DEBUG_MODE = True
DEFAULT_BRUSH_SIZE = 5
"""

from pathlib import Path
import yaml

# Path to the project root (two levels up from this file)
PROJECT_ROOT = Path(__file__).parent.parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"

if CONFIG_PATH.exists():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
else:
    print(f"Config file not found at {CONFIG_PATH}")

APP_NAME = data.get("APP_NAME", "QTPaint")
APP_VERSION = data.get("APP_VERSION", "VersionNotFound")
DEBUG_MODE = data.get("DEBUG_MODE", False)
DEFAULT_BRUSH_SIZE = data.get("DEFAULT_BRUSH_SIZE", 5)