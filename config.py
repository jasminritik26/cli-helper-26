import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "verbose": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "api_url": "https://api.example.com",
}

class ConfigLoader:
    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = Path(config_path) if config_path else Path("config.json")
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file, falling back to environment variables and defaults."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.config.update(file_config)
            except (json.JSONDecodeError, IOError):
                # Gracefully fallback to default values on error
                pass

        self._override_from_env()
        return self.config

    def _override_from_env(self) -> None:
        """Overrides configuration keys from environment variables prefixed with CLI_."""
        for key in self.config:
            env_key = f"CLI_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_val = DEFAULT_CONFIG[key]
                
                if isinstance(default_val, bool):
                    self.config[key] = val.lower() in ("true", "1", "yes", "on")
                elif isinstance(default_val, int):
                    try:
                        self.config[key] = int(val)
                    except ValueError:
                        pass
                else:
                    self.config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.config.get(key, default)
