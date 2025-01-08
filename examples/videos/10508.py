# Example of swapping variables without using a temporary variable in Python

# Initial values for a real-world use case
x = 10
y = 20

# Traditional swap using a temporary variable (inefficient)
# temp = x
# x = y
# y = temp

# Python hack: Swap variables without a temp variable using tuple unpacking
x, y = y, x

print(f"Swapped values: x = {x}, y = {y}")  # Output: x = 20, y = 10

# But, let's explore a more advanced scenario - swapping elements in a list:
data = [5, 10, 15, 20, 25]

# Swap the first and last elements
data[0], data[-1] = data[-1], data[0]

print("List after swapping first and last elements:", data)

# Applying this technique in a real-world problem like swapping coordinates:
point_a = (3, 5)
point_b = (7, 9)

# Swap points without using a temp variable
point_a, point_b = point_b, point_a

print("Swapped coordinates:")
print("Point A:", point_a)
print("Point B:", point_b)

# Another case: swapping dictionary keys and values
coordinates = {"latitude": 40.7128, "longitude": -74.0060}

# Swap keys and values (for specific cases like reversing a mapping)
coordinates = {v: k for k, v in coordinates.items()}

print("Swapped dictionary (coordinates):", coordinates)

# A deeper look into swapping values in a multidimensional array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Swap the first and last rows of the matrix
matrix[0], matrix[-1] = matrix[-1], matrix[0]

print("Matrix after swapping first and last rows:")
for row in matrix:
    print(row)

# Swap values in files
# Let's say we have two files '/tmp/test/input1.txt' and '/tmp/test/input2.txt'
# We want to swap their contents without using a temporary file

file1_path = '/tmp/test/input1.txt'
file2_path = '/tmp/test/input2.txt'

# Read contents of both files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()

# Swap contents by writing them back to the files
with open(file1_path, 'w') as file1, open(file2_path, 'w') as file2:
    file1.write(content2)
    file2.write(content1)

print(f"Contents of {file1_path} and {file2_path} have been swapped.")