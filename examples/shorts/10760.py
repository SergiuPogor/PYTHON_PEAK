import json

# JSON data from an API response (simulated as a string)
response_data = '{"name": "Alice", "age": 30, "active": true, "roles": ["admin", "user"]}'

# Load JSON string into a Python dictionary
data_dict = json.loads(response_data)

# Example 1: Access nested data easily
user_roles = data_dict["roles"]
print("User Roles:", user_roles)

# Example 2: Encode Python dictionary back to JSON format with pretty-printing
encoded_json = json.dumps(data_dict, indent=4)
print("Pretty-Printed JSON:\n", encoded_json)

# Example 3: Use custom separators for a more compact JSON
compact_json = json.dumps(data_dict, separators=(",", ":"))
print("Compact JSON:\n", compact_json)

# Example 4: Handling non-JSON serializable data
from datetime import datetime
data_dict["last_login"] = datetime.now()

try:
    # json.dumps will raise TypeError for non-serializable data (datetime here)
    print(json.dumps(data_dict))
except TypeError as e:
    print("Error:", e)

# Fix: Convert datetime to string before encoding
data_dict["last_login"] = data_dict["last_login"].isoformat()
encoded_json_with_date = json.dumps(data_dict)
print("JSON with last_login as ISO8601:\n", encoded_json_with_date)