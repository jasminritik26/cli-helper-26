import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {file_path}: {e}")

    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save config to {file_path}: {e}")