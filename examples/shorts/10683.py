# Example: Using zip to transpose a matrix

# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix using zip
transposed_matrix = list(zip(*matrix))

# Display the transposed result
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)

# Example 2: Transposing a list of coordinates
coordinates = [(1, 2), (3, 4), (5, 6)]

# Transpose the list of coordinates
transposed_coordinates = list(zip(*coordinates))

# Display the transposed coordinates
print("Transposed Coordinates:")
print(transposed_coordinates)