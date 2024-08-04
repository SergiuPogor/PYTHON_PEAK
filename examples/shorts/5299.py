def validate_age(age):
    # Check if the input is an integer
    if type(age) is not int:
        raise TypeError("Age must be an integer")
    # Further validation if needed
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

# Example usage
try:
    validate_age(25)  # Valid input
    validate_age("25")  # Invalid input
except (TypeError, ValueError) as e:
    print(e)