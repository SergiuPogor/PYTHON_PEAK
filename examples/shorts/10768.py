from typing import List, Dict

# Function to process user data with type hints
def process_user_data(users: List[Dict[str, str]]) -> None:
    # Loop through each user dictionary
    for user in users:
        # Print user details
        print(f"User Name: {user['name']}, Email: {user['email']}")

# Example user data
user_data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

# Call the function with user data
process_user_data(user_data)