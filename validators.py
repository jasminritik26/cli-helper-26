import re
from typing import Any, Optional

class InputValidator:
    """Centralized validation logic for cli-helper-26."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Verify email address format using regex."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def is_positive_integer(value: Any) -> bool:
        """Ensure value is a positive integer string."""
        try:
            int_val = int(value)
            return int_val > 0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_length(data: str, min_len: int, max_len: Optional[int] = None) -> bool:
        """Check if string length is within acceptable bounds."""
        length = len(data)
        if max_len is None:
            return length >= min_len
        return min_len <= length <= max_len

def sanitize_input(user_input: str) -> str:
    """Strip whitespace and normalize string inputs."""
    return user_input.strip() if isinstance(user_input, str) else ""