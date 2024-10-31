# Code Example: Using typing for Enhanced Code Documentation in Complex Structures

from typing import List, Dict, Optional, Union, TypedDict

# Define TypedDict to clarify expected structure in an API response
class UserData(TypedDict):
    id: int
    username: str
    email: str
    age: Optional[int]
    preferences: Dict[str, Union[str, int]]

def parse_user_data(data: List[UserData]) -> List[str]:
    """Extract usernames of active users over age 18."""
    return [user["username"] for user in data if user["age"] and user["age"] > 18]

# Example response from an API, now type-checked
response_data: List[UserData] = [
    {"id": 1, "username": "john_doe", "email": "john@example.com", "age": 21, 
     "preferences": {"theme": "dark", "notifications": 1}},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com", "age": None, 
     "preferences": {"theme": "light", "notifications": 0}},
    {"id": 3, "username": "bob_ross", "email": "bob@example.com", "age": 30, 
     "preferences": {"theme": "dark", "notifications": 1}}
]

# Extract valid usernames with clear, self-documenting code
active_usernames = parse_user_data(response_data)
print(f"Active Usernames: {active_usernames}")  # ["john_doe", "bob_ross"]