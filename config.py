import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file, merging with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        return config
        
    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass  # Graceful fallback to defaults on error
        
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)