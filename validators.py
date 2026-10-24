import re

def validate_input(user_input: str, min_length: int = 1, max_length: int = 50) -> bool:
    """Validates CLI input against length constraints and pattern requirements."""
    if not user_input or not isinstance(user_input, str):
        return False
    
    # Basic sanitization: check length
    if not (min_length <= len(user_input) <= max_length):
        return False
    
    # Prevent command injection by allowing only alphanumeric and basic symbols
    if not re.match(r'^[a-zA-Z0-9_\s-]+$', user_input):
        return False
        
    return True

def get_sanitized_input(prompt: str) -> str:
    """Prompts user and ensures input meets security standards."""
    while True:
        data = input(prompt).strip()
        if validate_input(data):
            return data
        print("Invalid input. Please use alphanumeric characters only.")