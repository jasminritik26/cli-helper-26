import json
from pathlib import Path
from typing import Any, Dict

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
    """Loads CLI configuration with default fallback support."""

    def __init__(self, config_path: str | None = None):
        self.config_path = Path(config_path) if config_path else self._get_default_path()
        self._config: Dict[str, Any] = {}

    def _get_default_path(self) -> Path:
        """Return default configuration file path based on OS location."""
        return Path.home() / ".config" / "cli-helper" / "config.json"

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, merging user settings with defaults."""
        merged_config = DEFAULT_CONFIG.copy()

        if not self.config_path.exists():
            self._config = merged_config
            return self._config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    merged_config.update(user_config)
        except (json.JSONDecodeError, OSError):
            # Fallback to default config on parse or read failure
            pass

        self._config = merged_config
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve specific configuration setting."""
        if not self._config:
            self.load()
        return self._config.get(key, default)
