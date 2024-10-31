# Using dataclasses.asdict for object serialization

from dataclasses import dataclass, asdict
import json

@dataclass
class User:
    name: str
    age: int
    email: str

def serialize_user(user: User) -> str:
    # Convert the User object to a dictionary
    user_dict = asdict(user)
    # Serialize the dictionary to a JSON string
    return json.dumps(user_dict)

if __name__ == "__main__":
    user = User(name="Alice", age=30, email="alice@example.com")
    user_json = serialize_user(user)
    print(user_json)  # Output: {"name": "Alice", "age": 30, "email": "alice@example.com"}