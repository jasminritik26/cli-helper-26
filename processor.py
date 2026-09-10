from typing import List, Dict, Optional, Any

class DataProcessor:
    """Handles transformation of raw input streams."""

    def __init__(self, delimiter: str = ",") -> None:
        self.delimiter: str = delimiter

    def process_lines(self, lines: List[str]) -> List[Dict[str, Any]]:
        """
        Splits input lines and converts them into structured dictionaries.
        
        :param lines: List of raw string inputs
        :return: List of parsed data mappings
        """
        processed_data: List[Dict[str, Any]] = []
        
        for index, line in enumerate(lines):
            if not line.strip():
                continue
            
            parts: List[str] = line.split(self.delimiter)
            entry: Dict[str, Any] = {
                "id": index,
                "raw": line.strip(),
                "count": len(parts)
            }
            processed_data.append(entry)
            
        return processed_data

    def get_summary(self, data: List[Dict[str, Any]]) -> Optional[str]:
        """
        Generates a summary string for the processed dataset.
        
        :param data: The list of parsed dictionaries
        :return: A formatted summary string or None if empty
        """
        if not data:
            return None
            
        total_items: int = len(data)
        return f"Processed {total_items} items successfully."