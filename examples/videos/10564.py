# Using format_map() with dictionaries in Python
def main():
    # Define a dictionary with placeholder values
    data = {
        'name': 'Alice',
        'age': 30,
        'city': 'Wonderland'
    }
    
    # Create a string template using placeholders
    template = "My name is {name}, I am {age} years old, and I live in {city}."

    # Using format_map to substitute values from the dictionary
    formatted_string = template.format_map(data)
    print(formatted_string)  # Output: My name is Alice, I am 30 years old, and I live in Wonderland.

    # Example with missing keys in the dictionary
    partial_data = {
        'name': 'Bob',
        'city': 'Builderland'
    }
    
    # Use the missing key with a default value
    template_with_default = "My name is {name}, I am {age:unknown} years old, and I live in {city}."
    
    # Substituting values using format_map with missing data
    formatted_string_with_default = template_with_default.format_map(partial_data)
    print(formatted_string_with_default)  
    # Output: My name is Bob, I am unknown years old, and I live in Builderland.

if __name__ == "__main__":
    main()

# This example illustrates how to use format_map() for both complete and partial data in Python.