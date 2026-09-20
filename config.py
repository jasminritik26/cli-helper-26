import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "port": 8080,
    "debug": False,
    "log_level": "INFO"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persist configuration to JSON file."""
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)