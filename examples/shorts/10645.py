# Custom sorting logic using the key parameter in sorted()
# Sample data: list of dictionaries representing users
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 30}
]

# Sort users by age
sorted_users_by_age = sorted(users, key=lambda user: user['age'])

# Sort users by name
sorted_users_by_name = sorted(users, key=lambda user: user['name'])

# Print sorted results
print("Sorted by age:")
for user in sorted_users_by_age:
    print(user)

print("\nSorted by name:")
for user in sorted_users_by_name:
    print(user)

# Example of sorting with multiple criteria (age, then name)
sorted_users_multiple = sorted(users, 
                                key=lambda user: (user['age'], user['name']))

print("\nSorted by age and then name:")
for user in sorted_users_multiple:
    print(user)