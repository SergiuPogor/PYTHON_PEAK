import json
from datetime import datetime

# Custom serializer for datetime objects
def custom_json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Type {type(obj).__name__} not serializable')

# Sample data with a datetime object
data = {
    "name": "Alice",
    "email": "alice@example.com",
    "last_login": datetime.now()
}

# Serializing the data with the custom serializer
json_data = json.dumps(data, default=custom_json_serializer)

# Output the serialized JSON
print(json_data)