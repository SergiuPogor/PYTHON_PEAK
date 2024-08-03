# Example of using Python's list() function for type conversion

# Sample data
data_set = {1, 2, 3, 4, 5}
data_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert set to list
list_from_set = list(data_set)
print("List from set:", list_from_set)

# Convert dictionary keys to list
list_from_dict_keys = list(data_dict.keys())
print("List from dictionary keys:", list_from_dict_keys)

# Convert dictionary values to list
list_from_dict_values = list(data_dict.values())
print("List from dictionary values:", list_from_dict_values)

# Convert dictionary items to list of tuples
list_from_dict_items = list(data_dict.items())
print("List from dictionary items:", list_from_dict_items)