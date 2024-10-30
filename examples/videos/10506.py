class OptimizedClass:
    __slots__ = ['name', 'age', 'occupation']  # Only these attributes are allowed

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

# Example: Creating multiple instances to show memory efficiency
people = [OptimizedClass(f"Person {i}", i+20, "Engineer") for i in range(10000)]

# Comparison: Class without __slots__ 
class NormalClass:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

# Demonstrating the memory impact
import sys

normal_instance = NormalClass("John Doe", 30, "Developer")
optimized_instance = OptimizedClass("Jane Doe", 29, "Designer")

# Memory usage comparison
print(f"Memory used by normal class: {sys.getsizeof(normal_instance)} bytes")
print(f"Memory used by optimized class: {sys.getsizeof(optimized_instance)} bytes")

# The memory difference is significant when dealing with thousands of instances!
# Now imagine working with millions of objects; __slots__ can save you from hitting memory limits.

# Trying to add an attribute dynamically will raise an AttributeError
try:
    optimized_instance.new_attr = "Not allowed"
except AttributeError as e:
    print(f"Error: {e}")

# However, with the normal class, adding attributes dynamically is allowed
normal_instance.new_attr = "Allowed"
print(f"New attribute added to normal class: {normal_instance.new_attr}")

# Example of a case where __slots__ shines
# File '/tmp/test/input.txt' contains large data to process
with open('/tmp/test/input.txt', 'r') as file:
    lines = file.readlines()

# Let's map lines of the file into optimized objects
class Line:
    __slots__ = ['index', 'content']
    
    def __init__(self, index, content):
        self.index = index
        self.content = content

file_lines = [Line(i, line.strip()) for i in range(len(lines))]
for line_obj in file_lines[:5]:  # Showing first 5 processed lines
    print(f"Line {line_obj.index}: {line_obj.content}")