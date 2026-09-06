import sys

def validate_input(user_input):
    """Checks if input is a non-empty string and not numeric."""
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty."
    if user_input.isdigit():
        return False, "Input cannot be a number."
    return True, ""

def run_processing_loop():
    """Main execution loop with input validation."""
    print("Starting cli-helper-26 processor. Type 'exit' to quit.")
    
    while True:
        try:
            raw_data = input(">>> ").strip()
            
            if raw_data.lower() == 'exit':
                print("Exiting processor.")
                break
                
            is_valid, error_msg = validate_input(raw_data)
            
            if not is_valid:
                print(f"Validation error: {error_msg}")
                continue
                
            # Processing logic
            result = raw_data.upper()
            print(f"Result: {result}")
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            break

if __name__ == '__main__':
    run_processing_loop()