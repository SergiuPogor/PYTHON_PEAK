import json
from datetime import datetime

class CustomObject:
    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

def custom_serializer(obj):
    """Custom serializer for handling specific object types."""
    if isinstance(obj, CustomObject):
        return {
            'name': obj.name,
            'created_at': obj.created_at.isoformat()
        }
    raise TypeError(f'Type {type(obj)} not serializable')

def main():
    # Create an instance of CustomObject
    my_object = CustomObject("Test Object", datetime.now())

    # Serialize the object using custom_serializer
    serialized_data = json.dumps(my_object, default=custom_serializer, indent=4)

    print("Serialized Custom Object:")
    print(serialized_data)

if __name__ == "__main__":
    main()