from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    email: str
    age: int = field(default=18)

    def __post_init__(self):
        if not self.username:
            raise ValueError("Username cannot be empty.")
        if "@" not in self.email:
            raise ValueError("Invalid email address.")
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

# Example usage
try:
    user1 = User(username='JohnDoe', email='john.doe@example.com', age=25)
    print(f"User created: {user1}")
    
    user2 = User(username='', email='invalid_email', age=-5)  # This will raise an error
except ValueError as e:
    print(e)