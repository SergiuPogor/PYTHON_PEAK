import json
from typing import Any

# Sample deeply nested JSON structure loaded from a file
with open('/tmp/test/input.json', 'r') as file:
    data = json.load(file)

# Recursive function to safely access nested data
def get_nested(data: dict, path: list[str], default: Any = None) -> Any:
    for key in path:
        try:
            data = data[key]
        except (KeyError, TypeError, IndexError):
            return default
    return data

# Example usage of get_nested function
address_path = ["user", "details", "contact", "address", "street"]
name_path = ["user", "name"]

street = get_nested(data, address_path, default="Street not found")
name = get_nested(data, name_path, default="Name not found")

print("User Name:", name)
print("User Street Address:", street)

# Advanced example - iterating over multiple nested elements
def extract_nested_values(data: dict, keys: list[str]) -> list[Any]:
    results = []
    for key_path in keys:
        value = get_nested(data, key_path)
        results.append(value)
    return results

# Define multiple paths to extract
paths = [
    ["user", "details", "contact", "email"],
    ["user", "details", "contact", "phone"],
    ["user", "details", "contact", "address", "city"],
    ["user", "preferences", "notifications", "email"],
]

extracted_values = extract_nested_values(data, paths)

# Display results
for path, value in zip(paths, extracted_values):
    print(" -> ".join(path) + ":", value)

# Example for handling lists within JSON with mixed depths
def handle_list_elements(data: dict, path: list[str]) -> list[Any]:
    result = get_nested(data, path, default=[])
    if isinstance(result, list):
        return [get_nested(item, ["street"], "No street") for item in result]
    return [result]

# Handling nested list elements
addresses_path = ["user", "addresses"]
street_addresses = handle_list_elements(data, addresses_path)
print("Street Addresses in list:", street_addresses)