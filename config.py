import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30
}

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config_path: str, config: Dict[str, Any]) -> None:
    """
    Persists configuration dictionary to a JSON file.
    """
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)