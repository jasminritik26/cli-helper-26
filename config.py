import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "debug": False,
    "timeout": 30,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persist configuration to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")