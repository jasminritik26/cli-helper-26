import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Handles loading of configuration files with default fallbacks and environment overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a JSON file and merges it with current settings.

        If the file does not exist, it preserves the defaults.
        """
        if not os.path.exists(filepath):
            return self.config

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    self.config.update(file_config)
        except (json.JSONDecodeError, IOError) as err:
            raise ValueError(
                f"Failed to parse config file at {filepath}: {err}"
            )

        return self.config

    def apply_env_overrides(self, prefix: str = "CLI_") -> Dict[str, Any]:
        """Overrides configuration values with environment variables starting with a prefix."""
        for key in self.config.keys():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                current_val = self.config[key]
                if isinstance(current_val, bool):
                    self.config[key] = val.lower() in ("true", "1", "yes")
                elif isinstance(current_val, int):
                    self.config[key] = int(val)
                elif isinstance(current_val, float):
                    self.config[key] = float(val)
                else:
                    self.config[key] = val
        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)
