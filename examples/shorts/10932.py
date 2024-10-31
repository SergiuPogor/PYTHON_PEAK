import importlib

def dynamic_import(module_name):
    try:
        # Dynamically import the specified module
        module = importlib.import_module(module_name)
        print(f"{module_name} imported successfully!")
        return module
    except ModuleNotFoundError:
        print(f"Module {module_name} not found!")

def main():
    # Example usage of dynamic_import function
    module_to_import = "math"  # Replace with any module name
    math_module = dynamic_import(module_to_import)
    
    if math_module:
        # Using the imported module
        result = math_module.sqrt(16)
        print(f"Square root of 16 is: {result}")

if __name__ == "__main__":
    main()