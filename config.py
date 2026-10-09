import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configuration."""
    
    def __init__(self, defaults: Dict[str, Any], config_path: str = "config.json"):
        self.defaults = defaults
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.defaults
        
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                # Merge user config over defaults
                return {**self.defaults, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

# Example usage initialization
default_settings = {
    "log_level": "INFO",
    "timeout": 30,
    "retries": 3
}

config_instance = ConfigLoader(default_settings)