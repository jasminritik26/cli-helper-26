import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "cli-helper",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "output_format": "json",
    "max_retries": 3,
    "timeout": 30,
}

class ConfigLoader:
    """Manages application configuration loading with fallback defaults."""

    def __init__(self, config_path: Optional[str] = None):
        if config_path:
            self.config_path = Path(config_path)
        else:
            self.config_path = Path.home() / ".cli_helper_config.json"
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Load user configuration merged with default settings."""
        merged_config = DEFAULT_CONFIG.copy()
        if self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        merged_config.update(user_config)
            except (json.JSONDecodeError, OSError):
                pass
        return merged_config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.config.get(key, default)

    def save() -> bool:
        """Save current configuration state to disk."""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except OSError:
            return False
