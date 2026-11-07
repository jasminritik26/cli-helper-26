import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG_PATH = Path.home() / ".cli_helper_config.json"


@dataclass
class AppConfig:
    """Stores global application settings for cli-helper."""

    verbose: bool = False
    timeout: int = 30
    output_format: str = "json"
    log_level: str = "INFO"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AppConfig":
        """Creates a config instance filtering out unknown keys."""
        valid_keys = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)


class ConfigManager:
    """Handles loading, saving, and updating application configuration."""

    def __init__(self, config_path: Optional[Path] = None) -> None:
        self.config_path = config_path or DEFAULT_CONFIG_PATH
        self.config = self.load_config()

    def load_config(self) -> AppConfig:
        """Loads configuration from JSON file or returns defaults."""
        if not self.config_path.exists():
            return AppConfig()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return AppConfig.from_dict(data)
        except (json.JSONDecodeError, OSError):
            return AppConfig()

    def save_config(self) -> bool:
        """Saves current configuration state to disk."""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(asdict(self.config), f, indent=2)
            return True
        except OSError:
            return False
