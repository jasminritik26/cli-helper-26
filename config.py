import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists current configuration to file."""
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # usage example
    settings = load_config()
    print(f"Loaded settings: {settings}")