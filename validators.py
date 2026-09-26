class ValidationError(Exception):
    """Custom exception for CLI input validation."""
    pass

def validate_input(user_input: str, expected_type: type) -> any:
    """Validate and cast user input based on expected type."""
    if not user_input or not user_input.strip():
        raise ValidationError("Input cannot be empty.")
    
    try:
        if expected_type == int:
            return int(user_input)
        elif expected_type == float:
            return float(user_input)
        elif expected_type == bool:
            normalized = user_input.lower()
            if normalized in ('true', '1', 'yes'):
                return True
            elif normalized in ('false', '0', 'no'):
                return False
            raise ValueError("Invalid boolean representation")
        return user_input.strip()
    except ValueError as e:
        raise ValidationError(f"Type mismatch: expected {expected_type.__name__}") from e

def process_command(cmd: str, params: list) -> dict:
    """Validate command parameters within the main loop."""
    if not cmd:
        raise ValidationError("Command cannot be empty")
    
    return {"cmd": cmd, "params": params}