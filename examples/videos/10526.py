import json
from datetime import datetime

# Custom encoder for complex data types
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format
        return super().default(obj)  # Call the default method for other types

# Sample data with a datetime object
data = {
    "name": "Alice",
    "age": 28,
    "joined": datetime(2023, 10, 30, 15, 30)
}

# Serialize data using the custom encoder
def serialize_data(data):
    try:
        json_data = json.dumps(data, cls=CustomJSONEncoder)
        print(json_data)  # Print the serialized JSON string
    except TypeError as e:
        print(f"Serialization error: {e}")

# Example usage of the serialize function
if __name__ == "__main__":
    serialize_data(data)