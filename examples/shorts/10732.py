from collections import defaultdict

# Function to combine multiple dictionaries without losing data
def combine_dictionaries(dicts):
    combined = defaultdict(list)  # Create a defaultdict with list as default type
    for d in dicts:
        for key, value in d.items():
            combined[key].append(value)  # Append value to the list for each key
    return dict(combined)  # Convert back to a regular dictionary

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'b': 4, 'c': 5}
dict3 = {'d': 6}

# Combine the dictionaries
result = combine_dictionaries([dict1, dict2, dict3])
print(result)  # Output: {'a': [1, 3], 'b': [2, 4], 'c': [5], 'd': [6]}