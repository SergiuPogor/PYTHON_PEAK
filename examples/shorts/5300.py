def combine_lists_to_dict(keys, values):
    # Check if lists are of the same length
    if len(keys) != len(values):
        raise ValueError("Both lists must be of the same length")
    # Combine lists into a dictionary
    return dict(zip(keys, values))

# Example usage
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

try:
    result = combine_lists_to_dict(keys, values)
    print(result)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
except ValueError as e:
    print(e)