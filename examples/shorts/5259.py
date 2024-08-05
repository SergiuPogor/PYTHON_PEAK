# Recursively count elements in nested data structures.
def count_nested_elements(data):    
    count = 0
    if isinstance(data, (list, dict)):
        if isinstance(data, list):
            for item in data:
                count += count_nested_elements(item)
        elif isinstance(data, dict):
            for key in data:
                count += count_nested_elements(data[key])
    else:
        return 1
    return count

# Example usage
nested_list = [1, [2, [3, 4]], 5]
nested_dict = {'a': [1, 2], 'b': {'c': [3, 4], 'd': 5}}
print("Count of elements in nested list:", count_nested_elements(nested_list))
print("Count of elements in nested dict:", count_nested_elements(nested_dict))

