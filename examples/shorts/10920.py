# Using the inspect module to analyze function signatures
import inspect

# Sample function to demonstrate inspect usage
def example_function(a: int, b: str = "default") -> str:
    """
    This is a simple example function.
    It takes an integer and a string and returns a formatted string.
    """
    return f"Number: {a}, String: {b}"

# Analyze the function signature using inspect
signature = inspect.signature(example_function)

# Display function name and signature
print(f"Function Name: {example_function.__name__}")
print(f"Function Signature: {signature}")

# Iterate over parameters in the function signature
for param in signature.parameters.values():
    print(f"Parameter: {param.name}, Type: {param.annotation}, Default: {param.default}")

# Analyze return type
return_type = signature.return_annotation
print(f"Return Type: {return_type}")