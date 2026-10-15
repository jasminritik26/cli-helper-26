import os
from typing import Dict, Any, Optional

class Config:
    """Handles application configuration loading and management."""

    def __init__(self, env_prefix: str = "CLI_") -> None:
        self.env_prefix: str = env_prefix
        self._settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Populates settings from environment variables with matching prefix."""
        for key, value in os.environ.items():
            if key.startswith(self.env_prefix):
                clean_key = key[len(self.env_prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Updates a configuration value."""
        self._settings[key] = value

    def __repr__(self) -> str:
        return f"Config(keys={list(self._settings.keys())})"

def get_default_config() -> Config:
    """Factory function for standard config initialization."""
    config = Config()
    config.set("debug", False)
    config.set("version", "1.0.0")
    return config