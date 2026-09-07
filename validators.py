import re

def validate_input(user_input, pattern=r'^[a-zA-Z0-9_\s]+$'):
    """Validates user input against a regex pattern."""
    if not user_input or not isinstance(user_input, str):
        return False, "Input cannot be empty."
    
    if not re.match(pattern, user_input):
        return False, "Input contains invalid characters."
    
    return True, "Success"

def process_main_loop():
    """Main loop for cli-helper-26 input processing."""
    while True:
        user_data = input("cli-helper-26> ")
        if user_data.lower() in ['exit', 'quit']:
            break

        is_valid, message = validate_input(user_data)
        if not is_valid:
            print(f"Validation error: {message}")
            continue

        # Process validated input here
        print(f"Processing: {user_data}")

if __name__ == "__main__":
    process_main_loop()