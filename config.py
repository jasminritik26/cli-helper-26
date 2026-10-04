import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file, merging with system defaults.
    Returns the populated dictionary.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {config_path}: {e}")
            
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """
    Persists current configuration dictionary to JSON file.
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save config to {config_path}: {e}")