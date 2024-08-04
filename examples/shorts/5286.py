# Advanced use of list() with nested data structures

# Example: Converting a list of tuples into a list of lists
data = [(1, 2), (3, 4), (5, 6)]
list_of_lists = list(map(list, data))
print(f"List of lists: {list_of_lists}")

# Example: Flattening a nested list of lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(f"Flattened list: {flattened_list}")

# Example: Using list() with dictionary values
dict_data = {'a': 1, 'b': 2, 'c': 3}
values_list = list(dict_data.values())
print(f"Values as list: {values_list}")

# Example: Handling large data efficiently
large_data = range(1_000_000)
list_data = list(large_data)
print(f"Length of list: {len(list_data)}")