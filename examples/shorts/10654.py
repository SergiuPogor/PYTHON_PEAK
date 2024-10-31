# Merging dictionaries in Python using the unpacking operator

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # Merge two dictionaries into one using unpacking
    return {**dict1, **dict2}

# Example usage
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

merged_dict = merge_dictionaries(dict_a, dict_b)

print("Merged Dictionary:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Merging multiple dictionaries
dict_c = {'d': 5}
dicts_to_merge = [dict_a, dict_b, dict_c]

# Using a loop to merge multiple dictionaries
final_dict = {}
for d in dicts_to_merge:
    final_dict = {**final_dict, **d}

print("Final Merged Dictionary:", final_dict)  # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5}