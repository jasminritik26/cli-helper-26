import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles batch processing and data sanitization for cli-helper-26."""

    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings

    def sanitize_input(self, data: str) -> str:
        """Remove trailing whitespace and control characters."""
        if not isinstance(data, str):
            return ""
        return data.strip().replace('\n', ' ').replace('\r', '')

    def process_batch(self, items: List[str]) -> List[str]:
        """Clean and filter a list of strings based on configuration."""
        results = []
        for item in items:
            cleaned = self.sanitize_input(item)
            if cleaned:
                results.append(cleaned)
        
        logger.info(f"processed {len(results)} items successfully")
        return results

    @staticmethod
    def format_output(data: List[str]) -> str:
        """Convert processed list into a readable string format."""
        return "\n".join([f"* {item}" for item in data])