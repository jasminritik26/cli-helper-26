from typing import List, Dict, Optional, Any

class DataProcessor:
    """Handles transformation and validation of CLI input data."""

    def __init__(self, prefix: str = "cli-") -> None:
        self.prefix: str = prefix

    def sanitize_input(self, data: List[str]) -> List[str]:
        """Removes empty strings and applies prefixes to valid inputs."""
        return [f"{self.prefix}{item.strip()}" for item in data if item.strip()]

    def format_results(self, items: List[str]) -> Dict[str, Any]:
        """Converts a list of items into a metadata dictionary."""
        return {
            "count": len(items),
            "items": items,
            "status": "processed"
        }

    def validate_keys(self, config: Dict[str, Any], required: List[str]) -> bool:
        """Checks if all required keys exist in the configuration dictionary."""
        return all(key in config for key in required)

    def process_batch(self, raw_data: Optional[List[str]]) -> Dict[str, Any]:
        """Main orchestration method for batch processing routines."""
        if not raw_data:
            return {"count": 0, "items": [], "status": "empty"}

        clean_data = self.sanitize_input(raw_data)
        return self.format_results(clean_data)