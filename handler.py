import sys

def validate_input(user_input):
    """Checks if input is non-empty and within character limits."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 255:
        return False, "Input exceeds 255 characters."
    return True, None

def main_loop():
    """Main processing loop for cli-helper-26."""
    print("CLI Helper v26. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                print("Exiting application.")
                break
            
            is_valid, error_msg = validate_input(user_input)
            
            if not is_valid:
                print(f"Validation error: {error_msg}")
                continue
                
            process_data(user_input)
        except EOFError:
            break

def process_data(data):
    """Placeholder for business logic processing."""
    print(f"Processing: {data}")

if __name__ == "__main__":
    main_loop()