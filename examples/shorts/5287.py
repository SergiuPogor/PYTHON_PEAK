# Advanced use of map() for complex data transformations

# Example: Applying a function to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Example: Converting a list of strings to uppercase
strings = ['python', 'map', 'function']
uppercased_strings = list(map(str.upper, strings))
print(f"Uppercased strings: {uppercased_strings}")

# Example: Combining elements of two lists element-wise
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(map(lambda x, y: x + y, list1, list2))
print(f"Combined list: {combined}")

# Example: Parsing integers from a list of numeric strings
numeric_strings = ['1', '2', '3', '4']
integers = list(map(int, numeric_strings))
print(f"Integers: {integers}")

# Example: Handling nested lists with map()
nested_lists = [[1, 2], [3, 4], [5, 6]]
flattened = list(map(lambda sublist: [x * 2 for x in sublist], nested_lists))
print(f"Flattened and doubled nested lists: {flattened}")