import re

def validate_input(user_input, pattern=r'^[a-zA-Z0-9_\s]+$'):
    """
    Validates user input against a regex pattern.
    Returns (bool, str) tuple indicating status and message.
    """
    if not user_input or not isinstance(user_input, str):
        return False, "input must be a non-empty string"
    
    if len(user_input) > 255:
        return False, "input exceeds maximum length of 255 characters"
    
    if not re.match(pattern, user_input):
        return False, "input contains invalid characters"
    
    return True, "success"

def process_main_loop():
    """
    Example main loop with integrated validation.
    """
    while True:
        data = input("Enter command (or 'exit' to quit): ").strip()
        if data.lower() == 'exit':
            break
        
        is_valid, message = validate_input(data)
        if not is_valid:
            print(f"Validation error: {message}")
            continue
        
        print(f"Processing: {data}")

if __name__ == "__main__":
    process_main_loop()