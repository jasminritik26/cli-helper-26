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
    """Loads configuration from JSON files and environment variables with defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Load file and environment overrides into base configuration."""
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                raise RuntimeError(f"Failed to load config file: {err}")

        # Apply environment variable overrides prefixed with CLI_
        for key in list(self.config.keys()):
            env_key = f"CLI_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if val.lower() in ("true", "false"):
                    self.config[key] = val.lower() == "true"
                elif val.isdigit():
                    self.config[key] = int(val)
                else:
                    self.config[key] = val

        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key with fallback."""
        return self.config.get(key, default)


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Utility function to quickly load configuration."""
    return ConfigLoader(config_path).config
