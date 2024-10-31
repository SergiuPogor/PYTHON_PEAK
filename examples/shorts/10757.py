from collections import defaultdict

# Basic usage: counting occurrences of items
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
count = defaultdict(int)
for item in items:
    count[item] += 1
print("Count of each item:", count)

# Advanced use-case: organizing user data by department
user_data = [
    ('John Doe', 'Engineering'),
    ('Jane Smith', 'HR'),
    ('Alice Brown', 'Engineering'),
    ('Bob White', 'Marketing')
]

# defaultdict with list to store multiple values per key
department_users = defaultdict(list)
for name, dept in user_data:
    department_users[dept].append(name)

print("\nUsers grouped by department:", department_users)

# Complex structure: initial nested defaultdict for hierarchical data
nested_data = defaultdict(lambda: defaultdict(int))

# Example of logging errors by type and severity
error_logs = [
    ('404', 'low'), ('500', 'high'), ('403', 'medium'),
    ('500', 'high'), ('404', 'low')
]

for error, severity in error_logs:
    nested_data[error][severity] += 1

print("\nError logs by type and severity:", dict(nested_data))