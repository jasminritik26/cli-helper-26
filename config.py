import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "debug": False,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file, merging with default values.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {filepath}: {e}. Using defaults.")
    
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Persists the current configuration state to a JSON file.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save config to {filepath}: {e}")