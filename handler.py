import re

def validate_input(data):
    """Check if the input data is valid.
    Returns (is_valid, error_message)
    """
    if not data:
        return False, "Input cannot be empty"
    data = data.strip()
    if len(data) < 3:
        return False, "Input must be at least 3 characters"
    if len(data) > 50:
        return False, "Input must be 50 characters or less"
    # Only allow alphanumeric and spaces
    if not re.match(r'^[a-zA-Z0-9 ]+$', data):
        return False, "Input can only contain letters, numbers, and spaces"
    return True, None

def process_data(data):
    """Process the validated data by capitalizing words."""
    data = data.strip().lower()
    words = data.split()
    processed = ' '.join(word.capitalize() for word in words)
    return processed

def main_loop():
    """Main processing loop implementing input validation."""
    print("CLI Helper - Data Processor")
    print("Enter text to process or 'exit' to quit.")
    processed_items = []
    while True:
        try:
            raw_input = input("> ").strip()
            if raw_input.lower() == 'exit':
                print("Exiting the program.")
                break
            # Input validation in the main processing loop
            is_valid, error_msg = validate_input(raw_input)
            if not is_valid:
                print(f"Invalid input: {error_msg}")
                continue
            # Process the valid input
            result = process_data(raw_input)
            processed_items.append(result)
            print(f"Result: {result}")
            print(f"Items processed so far: {len(processed_items)}")
        except EOFError:
            print("\nEnd of input. Exiting.")
            break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break
        except Exception as exc:
            print(f"Error during processing: {exc}")
            continue

if __name__ == "__main__":
    main_loop()