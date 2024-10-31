# Code Example: Using functools.wraps to Preserve Metadata

import functools

def preserve_metadata(func):
    @functools.wraps(func)  # Preserves metadata from the original function
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")  # Log function call
        return func(*args, **kwargs)  # Call the original function
    return wrapper

@preserve_metadata
def sample_function(x):
    """This function adds 5 to the input."""
    return x + 5

# Testing the function and its metadata
result = sample_function(10)
print(f"Result: {result}")
print(f"Function Name: {sample_function.__name__}")
print(f"Function Docstring: {sample_function.__doc__}")