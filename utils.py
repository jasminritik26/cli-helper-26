from typing import List, Dict, Any, Optional

def format_output(data: List[Dict[str, Any]], key: str = "name") -> List[str]:
    """
    Extracts values from a list of dictionaries based on a provided key.

    Args:
        data: A list of dictionaries containing string keys.
        key: The dictionary key to extract values from.

    Returns:
        A list of strings corresponding to the extracted values.
    """
    return [str(item.get(key, "")) for item in data if key in item]

def calculate_percentage(part: float, total: float, precision: int = 2) -> float:
    """
    Calculates percentage of a part relative to a total value.

    Args:
        part: The subset value.
        total: The whole value.
        precision: Number of decimal places for rounding.

    Returns:
        Calculated percentage as a float.
    """
    if total == 0:
        return 0.0
    return round((part / total) * 100, precision)

def sanitize_input(user_input: Optional[str]) -> str:
    """
    Cleans whitespace and handles None types for user input.

    Args:
        user_input: The raw string input from CLI.

    Returns:
        A stripped, non-null string representation.
    """
    if not user_input:
        return ""
    return user_input.strip()