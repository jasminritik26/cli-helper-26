from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles core data transformation logic for cli-helper-26."""

    def __init__(self, prefix: str = "cli-") -> None:
        self.prefix: str = prefix

    def sanitize_input(self, data: List[str]) -> List[str]:
        """Remove whitespace and filter by internal prefix."""
        return [item.strip() for item in data if item.startswith(self.prefix)]

    def format_output(self, payload: Dict[str, Any]) -> str:
        """Convert dictionary into a formatted key-value string."""
        if not payload:
            return "empty payload"
        
        items: List[str] = [f"{k}: {v}" for k, v in payload.items()]
        return " | ".join(items)

    def process_batch(self, items: List[Dict[str, Any]]) -> List[str]:
        """Transform a list of dictionaries into formatted strings."""
        results: List[str] = []
        for entry in items:
            processed: str = self.format_output(entry)
            results.append(processed)
        return results

def get_instance(namespace: Optional[str] = None) -> DataProcessor:
    """Factory function to generate processor instance."""
    return DataProcessor(prefix=namespace or "cli-")