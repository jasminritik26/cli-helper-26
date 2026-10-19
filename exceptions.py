class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class DataProcessingError(CLIHelperError):
    """Raised when data transformation fails."""
    pass

class ValidationError(CLIHelperError):
    """Raised when input data fails validation."""
    pass

def validate_data(data, schema_keys):
    """Utility to check if data contains required keys."""
    if not isinstance(data, dict):
        raise ValidationError("Data must be a dictionary")
    
    missing = [key for key in schema_keys if key not in data]
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")
    return True

def safe_get(data, key, default=None):
    """Safely retrieve values from nested dictionaries."""
    try:
        return data.get(key, default)
    except AttributeError:
        raise DataProcessingError(f"Invalid data structure for key access: {key}")