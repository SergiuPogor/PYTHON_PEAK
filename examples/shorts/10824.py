import sys

def get_caller_info():
    # Access the previous frame in the call stack
    frame = sys._getframe(1)
    
    # Get the name of the calling function
    caller_name = frame.f_code.co_name
    
    # Get the line number of the call
    line_number = frame.f_lineno
    
    return caller_name, line_number

def example_function():
    # Retrieve caller information
    caller_name, line_number = get_caller_info()
    print(f"Called by: {caller_name}, Line: {line_number}")

def another_function():
    example_function()

# Test the function to see the output
another_function()