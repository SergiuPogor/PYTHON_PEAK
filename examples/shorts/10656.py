# Transposing a matrix using zip function in Python

# Sample matrix to be transposed
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using zip to transpose the matrix
transposed = list(zip(*matrix))

# Output the transposed matrix
for row in transposed:
    print(row)  # Outputs: (1, 4, 7), (2, 5, 8), (3, 6, 9)

# Example of transposing a list of lists (more complex structure)
data = [
    ['Alice', 28, 'Engineer'],
    ['Bob', 24, 'Designer'],
    ['Charlie', 30, 'Teacher']
]

# Transpose the data
transposed_data = list(zip(*data))

# Display transposed data
for col in transposed_data:
    print(col)  # Outputs: ('Alice', 'Bob', 'Charlie'), (28, 24, 30), ('Engineer', 'Designer', 'Teacher')