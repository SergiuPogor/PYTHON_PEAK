# Example to prevent circular dependencies using a utility module
# Create a utility file to hold shared functionality
# utility.py
def common_function():
    return "This is a common function!"

# module_a.py
from utility import common_function

def function_a():
    result = common_function()
    return f"Function A: {result}"

# module_b.py
from utility import common_function

def function_b():
    result = common_function()
    return f"Function B: {result}"

# main.py
from module_a import function_a
from module_b import function_b

if __name__ == "__main__":
    print(function_a())
    print(function_b())