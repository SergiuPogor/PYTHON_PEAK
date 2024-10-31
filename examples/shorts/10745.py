from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    age: int = field(default=0)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.username:
            raise ValueError("Username cannot be empty!")
        if not (0 < self.age < 120):
            raise ValueError("Age must be between 1 and 119.")

def main():
    try:
        user1 = User(username="john_doe", age=25)  # Valid user
        print("User created:", user1)

        user2 = User(username="", age=30)  # Invalid user, raises ValueError
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()  # Execute the main function