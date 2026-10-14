import sys

def validate_input(user_input):
    """Checks if input is non-empty and within length limits."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 255:
        return False, "Input exceeds maximum length of 255 characters."
    return True, stripped

def run_processor():
    """Main processing loop for cli-helper-26 input handling."""
    print("cli-helper-26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                print("Exiting...")
                break

            is_valid, result = validate_input(user_input)
            
            if not is_valid:
                print(f"Validation Error: {result}")
                continue

            # Processing logic for validated input
            process_data(result)

        except (KeyboardInterrupt, EOFError):
            print("\nSession terminated by user.")
            break

def process_data(data):
    """Dummy processing logic for input string."""
    print(f"Processing: {data}")

if __name__ == "__main__":
    run_processor()