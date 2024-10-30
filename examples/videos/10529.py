import inspect

def example_function(a, b, c=5, *args, **kwargs):
    """A sample function for demonstration."""
    return a + b + c + sum(args)

def analyze_function(func):
    # Get the signature of the function
    signature = inspect.signature(func)
    print(f"Function: {func.__name__}")
    print("Signature:", signature)

    for name, param in signature.parameters.items():
        print(f"Parameter: {name}, Default: {param.default}, Kind: {param.kind}")

if __name__ == "__main__":
    analyze_function(example_function)

    # Example with a lambda function
    lambda_function = lambda x, y=10: x + y
    analyze_function(lambda_function)

    # Analyze a built-in function
    analyze_function(sum)