# List of dictionaries representing user profiles
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie"},  # Missing 'age' key
    {"name": "Diana", "age": 22}
]

# Sort by 'age', handling missing keys
sorted_users = sorted(users, key=lambda x: x.get('age', float('inf')))

# Print sorted result
for user in sorted_users:
    print(user)  # Output will be sorted by age