import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "verbose": False,
    "timeout": 30,
    "max_retries": 3,
    "log_level": "INFO",
    "cache_dir": "~/.cli_helper_cache"
}

class ConfigLoader:
    """Handles loading, merging, and accessing CLI helper configurations."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self._config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configurations from file, fallback to defaults on error."""
        if not os.path.exists(self.filepath):
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                user_config = json.load(file)
                if isinstance(user_config, dict):
                    self._config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Suppress errors to ensure the default config remains usable
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a value from the loaded configuration."""
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        """Returns the complete configuration dictionary."""
        return self._config.copy()