import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Centralized configuration management for cli-helper-26."""
    
    def __init__(self, env: str = "development"):
        self.env = env
        self.base_dir = Path(__file__).resolve().parent
        self.settings: Dict[str, Any] = {
            "debug": env == "development",
            "log_level": "INFO",
            "timeout": 30
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self.settings.get(key, default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Apply environment overrides to settings."""
        self.settings.update(new_settings)

    @classmethod
    def from_env(cls) -> 'Config':
        """Factory method for environment based initialization."""
        env = os.getenv("APP_ENV", "development")
        instance = cls(env=env)
        if env == "production":
            instance.update({"log_level": "ERROR", "timeout": 60})
        return instance