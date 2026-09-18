import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "verbose": False,
    "timeout": 30,
    "max_retries": 3,
    "output_format": "text",
    "api_url": "https://api.example.com/v1"
}

class ConfigLoader:
    """Loads and manages application configuration with default fallback values."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file and merges it with defaults."""
        if not os.path.exists(self.filepath):
            return self.config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    # Merge loaded config into defaults
                    for key, value in file_config.items():
                        if key in self.config:
                            self.config[key] = value
        except (json.JSONDecodeError, OSError):
            # Fallback silently to defaults if loading fails
            pass

        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)

    def save(self) -> bool:
        """Saves current configuration back to the file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except OSError:
            return False
