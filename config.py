import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "cli-helper",
    "version": "0.1.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "output_format": "json",
}


class ConfigLoader:
    """Loads configuration settings from files and environment variables with defaults."""

    def __init__(self, config_path: Path | str | None = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.reload()

    def reload(self) -> Dict[str, Any]:
        """Reload config from disk and apply environment overrides."""
        self._config = DEFAULT_CONFIG.copy()
        
        # Override with file configuration if present
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        self._config.update(file_data)
            except (json.JSONDecodeError, OSError):
                pass

        # Override with CLI_ prefixed environment variables
        for key in list(self._config.keys()):
            env_var = f"CLI_{key.upper()}"
            if env_var in os.environ:
                self._config[key] = self._cast_value(
                    os.environ[env_var], type(self._config[key])
                )

        return self._config

    def _cast_value(self, val: str, target_type: type) -> Any:
        """Cast environment string values to the matching target type."""
        if target_type == bool:
            return val.lower() in ("true", "1", "yes", "on")
        if target_type == int:
            try:
                return int(val)
            except ValueError:
                return val
        return val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Return full copy of active configuration."""
        return self._config.copy()
