# Working with a nested list using list comprehension: Flattening, Filtering, and Transforming

# Sample nested list with names and ages grouped in sublists
data = [
    ["Alice", 25], ["Bob", 19], ["Cara", 30],
    ["Dan", 17], ["Eve", 22], ["Frank", 27]
]

# Flatten and filter: Select names of those older than 20
filtered_names = [name for name, age in data if age > 20]
print("Filtered names:", filtered_names)

# Example with a matrix of integers, transforming values
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Double each number in the matrix and flatten the list
flattened_transformed = [num * 2 for row in matrix for num in row]
print("Doubled and flattened matrix:", flattened_transformed)

# Filtering nested lists by specific conditions: even numbers only
filtered_even = [[num for num in row if num % 2 == 0] for row in matrix]
print("Even numbers in matrix:", filtered_even)

# Example output:
# Filtered names: ['Alice', 'Cara', 'Eve', 'Frank']
# Doubled and flattened matrix: [2, 4, 6, 8, 10, 12, 14, 16, 18]
# Even numbers in matrix: [[2], [4, 6], [8]]