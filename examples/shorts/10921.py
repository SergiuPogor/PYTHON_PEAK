# Dynamically importing a module using importlib
import importlib

# Function to import a module based on its string name
def dynamic_import(module_name: str):
    try:
        # Dynamically import the specified module
        module = importlib.import_module(module_name)
        return module
    except ModuleNotFoundError as e:
        print(f"Error: {e}")
        return None

# Example usage: Importing the 'math' module dynamically
math_module = dynamic_import("math")

# If successfully imported, use the module
if math_module:
    # Calculate square root using the dynamically imported module
    result = math_module.sqrt(16)
    print(f"The square root of 16 is: {result}")

# Example of a nonexistent module
invalid_module = dynamic_import("nonexistent_module")