def context_dependent_decorator(context):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if context == 'development':
                print("Running in development mode.")
                # Custom behavior for development
                return func(*args, debug=True, **kwargs)
            elif context == 'production':
                print("Running in production mode.")
                # Custom behavior for production
                return func(*args, debug=False, **kwargs)
            else:
                raise ValueError("Unknown context")
        return wrapper
    return decorator

@context_dependent_decorator(context='development')
def process_data(data, debug=False):
    if debug:
        print(f"Debugging data: {data}")
    # Process the data
    return f"Processed {data}"

# Example usage
result = process_data("Sample Data")
print(result)

@context_dependent_decorator(context='production')
def analyze_data(data, debug=False):
    if debug:
        print(f"Analyzing data: {data}")
    # Analyze the data
    return f"Analyzed {data}"

# Example usage
result = analyze_data("Production Data")
print(result)