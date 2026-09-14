import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of configuration files with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Overwrites default values with those found in the JSON file."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {filepath}: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a value from the configuration."""
        return self.config.get(key, default)

def create_config_manager(defaults: Dict[str, Any], path: str = 'config.json') -> ConfigLoader:
    """Factory function to initialize config loader."""
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    return loader