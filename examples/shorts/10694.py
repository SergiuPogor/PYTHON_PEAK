import json
from datetime import datetime

# Custom JSON Encoder
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format
        if hasattr(obj, '__dict__'):
            return obj.__dict__  # Convert objects to their __dict__ representation
        return super().default(obj)  # Call the default method for other types

# Example data class
class User:
    def __init__(self, name, signup_date):
        self.name = name
        self.signup_date = signup_date

# Creating a user instance
user = User("Alice", datetime(2024, 1, 15, 10, 30))

# Serializing the user instance using the custom encoder
user_json = json.dumps(user, cls=CustomJSONEncoder)

# Output the serialized JSON
print(user_json)  # {"name": "Alice", "signup_date": "2024-01-15T10:30:00"}