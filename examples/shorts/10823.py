import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)

# Decorator for logging function calls
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function: {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Example function using the logging decorator
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

# Test the decorated functions
add(5, 10)
multiply(3, 7)