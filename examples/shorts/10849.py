class CustomError(Exception):
    # Custom exception class for specific errors
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def risky_operation(value):
    # Example function that may cause an error
    if value < 0:
        raise CustomError("Negative value error: Value must be positive.")
    return value ** 2

def main():
    test_values = [10, -5, 20]

    for val in test_values:
        try:
            result = risky_operation(val)
            print(f"The result for {val} is {result}")
        except CustomError as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()