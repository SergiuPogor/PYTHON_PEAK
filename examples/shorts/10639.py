# Example: Using namedtuple to create a structured, memory-efficient data format

from collections import namedtuple

# Define a simple data structure for a 3D point with named fields
Point3D = namedtuple("Point3D", ["x", "y", "z"])

# Create instances representing coordinates
p1 = Point3D(1.5, -2.4, 3.0)
p2 = Point3D(0.0, 7.2, -5.5)

# Access values by name for readability
print("Point 1 X-coordinate:", p1.x)
print("Point 1 Y-coordinate:", p1.y)

# Attempting to mutate will throw an error, making it immutable
try:
    p1.x = 10.0
except AttributeError as e:
    print("Error:", e)

# A more practical example: namedtuple for fast, organized data
FileRecord = namedtuple("FileRecord", ["filename", "size", "modified_date"])

record = FileRecord(filename="document.txt", size=2048, modified_date="2024-10-01")

# Access fields by name, ideal for structured read-only data
print("File:", record.filename, "| Size:", record.size, "| Date Modified:", record.modified_date)

# namedtuple is excellent for lightweight records where you need structure without creating full classes