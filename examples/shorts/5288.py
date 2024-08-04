# Advanced use of memoryview() for efficient data manipulation

# Create a large bytearray
data = bytearray(b'Hello World! This is a test of memoryview.')

# Create a memoryview of the bytearray
view = memoryview(data)

# Modify data through the memoryview
view[0:5] = b'HELLO'

# Create a new memoryview to slice part of the data
slice_view = view[6:11]
print(f"Sliced data: {slice_view.tobytes().decode()}")  # Output: 'World'

# Working with a numpy array
import numpy as np

# Create a numpy array
array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Create a memoryview of the numpy array
array_view = memoryview(array)

# Modify data through the memoryview
array_view[0] = 10
print(f"Modified array: {array}")  # Output: [10  2  3  4  5]

# Using memoryview with binary file
with open('/tmp/test/input.bin', 'rb') as f:
    file_data = memoryview(f.read())

# Print file data in a human-readable format
print(f"File data: {file_data[:10]}")  # Show the first 10 bytes