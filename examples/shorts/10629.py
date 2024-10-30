# Dynamic variable naming with f-strings in a dictionary-based approach
prefix = "user_"
users = {}

# Define dynamic variables using f-strings
for i in range(1, 6):
    username = f"{prefix}{i}"
    users[username] = {"id": i, "status": "active"}

# Accessing variables dynamically
for user_key in users:
    user_id = users[user_key]["id"]
    user_status = users[user_key]["status"]
    print(f"{user_key}: ID={user_id}, Status={user_status}")

# Example use-case: Updating a specific dynamic variable
target_user_id = 3
users[f"{prefix}{target_user_id}"]["status"] = "inactive"

# Checking updates
for user_key, info in users.items():
    print(f"{user_key} -> {info}")