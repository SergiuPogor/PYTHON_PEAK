# Example: Using uuid4() to generate unique identifiers for distributed systems

import uuid
import json

def generate_user_data(user_name):
    # Unique user_id generated with uuid4
    user_id = uuid.uuid4()
    return {
        "user_id": str(user_id),
        "name": user_name
    }

def save_unique_file(data, folder="/tmp/test"):
    # Unique filename created with uuid4
    file_id = uuid.uuid4()
    file_path = f"{folder}/data_{file_id}.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

# Usage
user_data = generate_user_data("Alice Smith")
file_path = save_unique_file(user_data)

print(f"Generated User Data: {user_data}")
print(f"File saved at: {file_path}")

# Another use-case: Generating unique session tokens
def create_session_token():
    return str(uuid.uuid4())

session_token = create_session_token()
print(f"Unique Session Token: {session_token}")