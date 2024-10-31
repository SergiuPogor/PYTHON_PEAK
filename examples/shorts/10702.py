from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    age: int = 0  # default value for age

# Example usage
if __name__ == "__main__":
    user1 = User("john_doe", "john@example.com", 30)
    user2 = User("jane_doe", "jane@example.com")  # age defaults to 0
    
    print(user1)  # Output: User(username='john_doe', email='john@example.com', age=30)
    print(user2)  # Output: User(username='jane_doe', email='jane@example.com', age=0)