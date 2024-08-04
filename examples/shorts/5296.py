# Example demonstrating advanced use of str() for complex data handling

def display_user_info(user_id, user_name, user_age):
    # Converts all data to string and formats output
    user_info = f"User ID: {str(user_id)}, Name: {str(user_name)}, Age: {str(user_age)}"
    return user_info


# Usage example with a complex data structure
user_data = {
    "id": 101,
    "name": "Alice",
    "age": 30
}

# Print formatted user info
print(display_user_info(user_data["id"], user_data["name"], user_data["age"]))

# Output: User ID: 101, Name: Alice, Age: 30
