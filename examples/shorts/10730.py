# Define multiple dictionaries
dict_a = {'name': 'Alice', 'age': 25}
dict_b = {'age': 30, 'city': 'New York'}
dict_c = {'hobby': 'painting', 'country': 'USA'}

# Merge dictionaries using the | operator (Python 3.9+)
merged_dict = dict_a | dict_b | dict_c

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)

# Output:
# Merged Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobby': 'painting', 'country': 'USA'}