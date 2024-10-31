# Directory structure: ensure files are under /tmp/test/
# Use case example for avoiding circular imports using importlib in large projects

# In /tmp/test/processor.py
def process_data(data):
    from importlib import import_module

    # Dynamically importing the function to avoid circular import issues
    utilities = import_module("test.utilities")
    processed = utilities.transform_data(data)
    return f"Processed: {processed}"

# In /tmp/test/utilities.py
def transform_data(data):
    from importlib import import_module

    # Another dynamic import to avoid circular import back to processor
    processor = import_module("test.processor")
    base = processor.process_data("base")
    return f"Transformed({data}) with base as {base}"

# Testing the circular import handling with importlib
if __name__ == "__main__":
    from test.processor import process_data
    
    result = process_data("Sample Data")
    print(result)