# Custom Exception Example using BaseException

# Define a custom exception
class CustomError(BaseException):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        return f'CustomError {self.error_code}: {self.message}'

# Function that raises the custom exception
def risky_operation(value):
    if value < 0:
        raise CustomError("Negative value not allowed!", 400)
    return value ** 2

# Example usage
try:
    result = risky_operation(-5)
except CustomError as e:
    print(e)  # Outputs: CustomError 400: Negative value not allowed!

# Another example to show different error code
try:
    result = risky_operation(10)
    print(f'Success: {result}')  # Outputs: Success: 100
except CustomError as e:
    print(e)