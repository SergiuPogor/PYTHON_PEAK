# Using frozenset for fast membership testing
# Define a frozenset of user IDs
user_ids = frozenset([1001, 1002, 1003, 1004, 1005])

# Function to check if a user ID is active
def is_user_active(user_id):
    return user_id in user_ids

# Testing the function with various user IDs
test_ids = [1001, 2001, 1003, 3000, 1005]

# Check and print the status of each test ID
for test_id in test_ids:
    if is_user_active(test_id):
        print(f"User ID {test_id} is active.")
    else:
        print(f"User ID {test_id} is not active.")

# Adding a new user ID (not possible with frozenset, demonstrates immutability)
try:
    user_ids.add(1006)  # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)