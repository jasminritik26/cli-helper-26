import re

def validate_input(user_input: str) -> bool:
    """
    Validates that input consists only of alphanumeric characters
    and meets length requirements.
    """
    if not user_input or len(user_input) > 50:
        return False
    
    # Pattern allows only letters and numbers
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, user_input))

def sanitize_input(user_input: str) -> str:
    """
    Removes leading/trailing whitespace to clean input.
    """
    return user_input.strip()

def get_validated_command(prompt_text: str) -> str:
    """
    Interactive loop to retrieve valid user input.
    """
    while True:
        user_data = input(prompt_text)
        clean_data = sanitize_input(user_data)
        
        if validate_input(clean_data):
            return clean_data
        
        print("Invalid input. Please use alphanumeric characters only.")