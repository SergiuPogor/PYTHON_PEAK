# Merging dictionaries using collections.ChainMap

from collections import ChainMap

# Define some sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

# Create a ChainMap to combine the dictionaries
combined = ChainMap(dict1, dict2, dict3)

# Accessing values from combined dictionaries
print(combined['a'])  # Output: 1 from dict1
print(combined['b'])  # Output: 2 from dict1 (first occurrence)
print(combined['c'])  # Output: 4 from dict2
print(combined['d'])  # Output: 5 from dict3

# Adding a new value to the first dictionary
combined['e'] = 6  # This will update dict1
print(dict1)  # Output: {'a': 1, 'b': 2, 'e': 6}