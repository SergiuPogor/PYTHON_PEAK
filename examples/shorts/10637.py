# Example: Using itertools.chain to efficiently chain multiple iterators

from itertools import chain

def read_multiple_files(*file_paths):
    # Chain iterators from multiple files to read lines as a single iterator
    return chain(*(open(file, "r") for file in file_paths))

# Paths for demonstration, e.g., `/tmp/test/input1.txt`, `/tmp/test/input2.txt`
file_paths = ["/tmp/test/input1.txt", "/tmp/test/input2.txt"]

# Using chained iterators to read all lines from multiple files at once
for line in read_multiple_files(*file_paths):
    print(line.strip())  # Processing each line without loading entire files

# Another use case: chaining multiple lists of data
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Chain multiple lists as a single iterator for processing
combined = list(chain(list1, list2, list3))
print("Combined List:", combined)

# Or, chaining dynamic ranges without memory overhead of concatenation
ranges = chain(range(10), range(20, 30), range(40, 50))
for num in ranges:
    print(num)