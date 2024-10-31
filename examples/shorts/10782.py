# Example of using functools.wraps to preserve metadata in decorators

from functools import wraps

# Decorator to log function execution
def logger(func):
    @wraps(func)  # Preserve the metadata of the original function
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")  # Log function name
        result = func(*args, **kwargs)  # Call the original function
        print(f"Executed: {func.__name__}")
        return result
    return wrapper

@logger
def add(a, b):
    """Add two numbers."""
    return a + b

@logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# Testing the functions
print(add(5, 3))  # Output: 8
print(multiply(4, 6))  # Output: 24

# Checking the metadata
print(add.__name__)  # Output: add
print(add.__doc__)  # Output: Add two numbers.
print(multiply.__name__)  # Output: multiply
print(multiply.__doc__)  # Output: Multiply two numbers.