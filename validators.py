import re

# regex patterns for standard input validation
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
POSITIVE_INT_PATTERN = r'^\d+$'

def validate_email(email: str) -> bool:
    """checks if email matches standard format"""
    return bool(re.match(EMAIL_PATTERN, email))

def validate_positive_integer(value: str) -> bool:
    """checks if string represents a non-negative integer"""
    return bool(re.match(POSITIVE_INT_PATTERN, value))

def get_validated_input(prompt: str, validator_func) -> str:
    """loops until valid input is provided by user"""
    while True:
        user_input = input(prompt).strip()
        if validator_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

if __name__ == '__main__':
    # usage in main processing loop
    email = get_validated_input("Enter your email: ", validate_email)
    age = get_validated_input("Enter your age: ", validate_positive_integer)
    print(f"Captured: {email}, {age}")