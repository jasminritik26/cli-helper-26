import os
import json
import sys
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "verbose": False,
    "max_retries": 3,
    "timeout": 30.0,
    "api_url": "https://api.cli-helper.local",
    "output_format": "json"
}

class ConfigLoader:
    """Loads configuration from a JSON file, falling back to defaults and environment variables."""

    def __init__(self, config_path: str | None = None):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration from file and applies environment overrides."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file ({err}). Using defaults.", file=sys.stderr)

        # Override with environment variables if present (prefixed with CLI_HELPER_)
        for key in self.config:
            env_key = f"CLI_HELPER_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_type = type(self.config[key])
                try:
                    if default_type is bool:
                        self.config[key] = val.lower() in ("true", "1", "yes", "on")
                    else:
                        self.config[key] = default_type(val)
                except ValueError:
                    pass

    def get(self, key: str) -> Any:
        """Retrieves a config value by its key."""
        return self.config.get(key)