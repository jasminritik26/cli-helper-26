import re
from typing import Dict, Any, Union

# Configuration constants for cli-helper-26
DEFAULT_ENCODING: str = 'utf-8'
LOG_LEVEL: str = 'INFO'

# Regex pattern for basic data sanitization
SANITIZATION_PATTERN = re.compile(r'[^a-zA-Z0-9_\-\s]')

def sanitize_input(data: str) -> str:
    """Removes restricted characters from input strings."""
    return SANITIZATION_PATTERN.sub('', data).strip()

def format_data_dict(data: Dict[str, Any]) -> Dict[str, str]:
    """Converts all dictionary values to sanitized strings."""
    return {str(k): sanitize_input(str(v)) for k, v in data.items()}

# Data handling status codes
STATUS_SUCCESS: int = 200
STATUS_ERROR: int = 500
STATUS_INVALID: int = 400

def get_status_message(code: int) -> str:
    """Maps integer status codes to descriptive messages."""
    messages = {
        200: "Operation completed successfully",
        500: "Internal server processing error",
        400: "Invalid data input provided"
    }
    return messages.get(code, "Unknown status code")