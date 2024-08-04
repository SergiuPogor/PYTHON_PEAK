# Practical use of enumerate() in a real-world scenario

# Example: Processing lines in a file and numbering them

file_path = '/tmp/test/input.txt'

try:
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            # Print the line number and content
            print(f"Line {index + 1}: {line.strip()}")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

# Example: Using enumerate() to track index in a list of tasks

tasks = ["read book", "write code", "test software", "deploy application"]

for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")

# Example: Using enumerate() with a list of dictionaries

employees = [
    {"name": "Alice", "role": "Developer"},
    {"name": "Bob", "role": "Designer"},
    {"name": "Charlie", "role": "Manager"}
]

for index, employee in enumerate(employees):
    print(f"Employee {index + 1}: {employee['name']} is a {employee['role']}")