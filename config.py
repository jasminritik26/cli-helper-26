import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "cli-helper",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "output_format": "json",
}


class ConfigLoader:
    """Manages loading application configuration with default fallbacks."""

    def __init__(self, config_path: Optional[Path] = None) -> None:
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.reload()

    def reload(self) -> Dict[str, Any]:
        """Reload configuration from file and environment overrides."""
        self._config = DEFAULT_CONFIG.copy()

        if self.config_path and self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as stream:
                    user_config = json.load(stream)
                    if isinstance(user_config, dict):
                        self._config.update(user_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Could not read config file ({err})")

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        """Override configuration options using environment variables."""
        if debug_env := os.getenv("CLI_DEBUG"):
            self._config["debug"] = debug_env.lower() in ("1", "true", "yes")
        if log_env := os.getenv("CLI_LOG_LEVEL"):
            self._config["log_level"] = log_env.upper()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration setting by key."""
        return self._config.get(key, default)

    @property
    def settings(self) -> Dict[str, Any]:"""Return a copy of active settings."""
        return self._config.copy()