import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "cli-helper",
    "version": "0.1.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "output_format": "json",
}


class ConfigLoader:
    """Loads and manages application configuration with default fallback values."""

    def __init__(self, config_path: Optional[str] = None):
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self.load_file(config_path)

    def load_file(self, filepath: str) -> None:
        """Load configuration settings from a JSON file."""
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"Config file not found: {filepath}")

        with open(path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                self._config.update(user_config)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set or override a configuration key."""
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return the active configuration dictionary."""
        return self._config.copy()