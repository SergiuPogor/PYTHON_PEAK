import sys

# A simple example function to demonstrate tracing
def example_function(x):
    return x * x

# Trace function to be set with sys.settrace
def trace_function(frame, event, arg):
    if event == 'line':
        line_no = frame.f_lineno
        filename = frame.f_code.co_filename
        print(f"Executing line {line_no} in {filename}")
    return trace_function

# Setting the trace function
def set_tracer():
    sys.settrace(trace_function)

if __name__ == "__main__":
    set_tracer()  # Start tracing

    # Execute some example code
    for i in range(5):
        result = example_function(i)
        print(f"Result for {i}: {result}")

    # Stop tracing
    sys.settrace(None)