import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from JSON file or return defaults."""
    if not os.path.exists(filepath):
        return defaults

    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
            # Deep merge defaults with loaded config
            final_config = defaults.copy()
            final_config.update(config)
            return final_config
    except (json.JSONDecodeError, IOError):
        return defaults

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persist configuration to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# Usage example for cli-helper-26
if __name__ == "__main__":
    default_settings = {
        "verbose": False,
        "retries": 3,
        "log_level": "INFO"
    }
    
    current_config = load_config("config.json", default_settings)
    print(f"Active configuration: {current_config}")