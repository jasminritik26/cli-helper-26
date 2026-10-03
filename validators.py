import re
from typing import Any, Optional

class InputValidator:
    """Utility class for standard CLI input validation."""

    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    @staticmethod
    def is_non_empty(value: Any) -> bool:
        """Verify that the input is not empty or whitespace only."""
        return bool(value and str(value).strip())

    @staticmethod
    def is_email(email: str) -> bool:
        """Check if string matches email format."""
        if not email:
            return False
        return bool(re.match(InputValidator.EMAIL_REGEX, email))

    @staticmethod
    def range_check(value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within specified bounds."""
        return min_val <= value <= max_val

def validate_input(data: Any, criteria: str) -> bool:
    """Proxy function for basic validation logic."""
    validator = InputValidator()
    if criteria == 'email':
        return validator.is_email(data)
    elif criteria == 'required':
        return validator.is_non_empty(data)
    return False