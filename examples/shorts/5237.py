# A real-world example of using any() in a Python application

# Function to check if a list of users contains any admins
def contains_admin(users):
    return any(user['is_admin'] for user in users)

# Sample data
users = [
    {'username': 'alice', 'is_admin': False},
    {'username': 'bob', 'is_admin': True},
    {'username': 'carol', 'is_admin': False}
]

# Check if there are any admins
if contains_admin(users):
    print("There is at least one admin.")
else:
    print("No admins found.")
