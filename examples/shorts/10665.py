# Check if any item in the list is positive
numbers = [-1, -2, 3, -4]
if any(num > 0 for num in numbers):
    print("There's at least one positive number!")

# Check if all items in the list are positive
if all(num > 0 for num in numbers):
    print("All numbers are positive!")
else:
    print("Not all numbers are positive!")

# A more complex example
students = [
    {"name": "Alice", "passed": True},
    {"name": "Bob", "passed": False},
    {"name": "Charlie", "passed": True}
]

# Check if any student passed
if any(student['passed'] for student in students):
    print("At least one student passed the exam.")

# Check if all students passed
if all(student['passed'] for student in students):
    print("All students passed the exam.")
else:
    print("Some students did not pass.")