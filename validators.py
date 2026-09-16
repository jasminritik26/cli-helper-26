import re
from typing import Any, Optional

class Validator:
    """Utility class for common CLI input validations."""
    
    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    @staticmethod
    def is_email(value: str) -> bool:
        """Check if input string follows standard email pattern."""
        return bool(re.match(Validator.EMAIL_REGEX, value))

    @staticmethod
    def is_positive_int(value: Any) -> bool:
        """Verify that value is a positive integer."""
        try:
            int_val = int(value)
            return int_val > 0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within inclusive boundaries."""
        return min_val <= value <= max_val

def validate_cli_input(value: str, type_check: str = "string") -> bool:
    """Dispatcher for common input validation tasks."""
    if type_check == "email":
        return Validator.is_email(value)
    elif type_check == "positive_int":
        return Validator.is_positive_int(value)
    return len(value.strip()) > 0