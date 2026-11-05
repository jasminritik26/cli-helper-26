class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class DataValidationError(CLIHelperError):
    """Raised when input data fails schema requirements."""
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

class DataProcessingError(CLIHelperError):
    """Raised when data transformation fails."""
    pass

def validate_payload(data: dict, required_keys: list):
    """Checks dict for required keys and raises errors."""
    if not isinstance(data, dict):
        raise DataValidationError("Payload must be a dictionary")
    
    for key in required_keys:
        if key not in data:
            raise DataValidationError(f"Missing required field: {key}", field=key)

def sanitize_input(data: str) -> str:
    """Removes whitespace and controls characters."""
    try:
        return " ".join(data.split()).strip()
    except Exception as e:
        raise DataProcessingError(f"Sanitization failed: {str(e)}")