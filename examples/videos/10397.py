class InvalidInputError(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message):
        super().__init__(message)

class CalculationError(Exception):
    """Custom exception for errors in calculations."""
    def __init__(self, message):
        super().__init__(message)

def divide_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise InvalidInputError("Both inputs must be numbers.")
    if num2 == 0:
        raise CalculationError("Division by zero is not allowed.")
    return num1 / num2

def main():
    try:
        result = divide_numbers(10, 0)
        print(f"Result: {result}")
    except InvalidInputError as e:
        print(f"Invalid Input: {e}")
    except CalculationError as e:
        print(f"Calculation Error: {e}")

if __name__ == "__main__":
    main()