import itertools

# Example of a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Flatten the nested list using itertools.chain
flat_list = list(itertools.chain.from_iterable(nested_list))

# Output the flattened list
print(flat_list)  # This will output: [1, 2, 3, 4, 5, 6, 7, 8, 9]