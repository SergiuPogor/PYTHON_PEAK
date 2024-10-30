from collections import defaultdict

def handle_nested_dict(data, keys):
    # Navigate through nested dictionaries safely
    current_level = data
    for key in keys:
        if isinstance(current_level, dict):
            # Use get to avoid KeyError
            current_level = current_level.get(key, {})
        else:
            # If current level is not a dict, return None
            return None
    return current_level

# Sample nested dictionary
nested_dict = {
    'user': {
        'name': 'Alice',
        'age': 30,
        'address': {
            'city': 'Wonderland'
        }
    }
}

# Example 1: Safe access to existing key
city = handle_nested_dict(nested_dict, ['user', 'address', 'city'])
print(f"City: {city}")  # Output: City: Wonderland

# Example 2: Safe access to missing key
postal_code = handle_nested_dict(nested_dict, ['user', 'address', 'postal_code'])
print(f"Postal Code: {postal_code}")  # Output: Postal Code: None

# Using defaultdict for default values
default_dict = defaultdict(lambda: 'Not Found')
default_dict.update({
    'name': 'Bob',
    'age': 25
})

# Accessing an existing key
print(f"Name: {default_dict['name']}")  # Output: Name: Bob

# Accessing a missing key
print(f"Country: {default_dict['country']}")  # Output: Country: Not Found

if __name__ == "__main__":
    pass  # This block is reserved for future code extensions