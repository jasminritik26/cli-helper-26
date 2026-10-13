import logging
from typing import List, Dict, Any

class DataProcessor:
    """Handles raw data cleanup and transformation tasks."""

    def __init__(self, debug: bool = False):
        self.logger = logging.getLogger(__name__)
        self.debug = debug

    def clean_records(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Removes empty keys and strips whitespace from string values."""
        cleaned = []
        for entry in data:
            if not isinstance(entry, dict):
                continue
            
            processed = {
                k: v.strip() if isinstance(v, str) else v 
                for k, v in entry.items() if v is not None
            }
            cleaned.append(processed)
        return cleaned

    def reformat_output(self, data: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
        """Organizes list of records into a structured format."""
        return {
            "metadata": {"count": len(data), "status": "processed"},
            "results": data
        }

def process_pipeline(raw_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Orchestrator for processor logic."""
    processor = DataProcessor()
    cleaned = processor.clean_records(raw_data)
    return processor.reformat_output(cleaned)