from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    age: int

def main():
    # Creating an instance of the User class
    user1 = User(username="john_doe", email="john@example.com", age=30)
    user2 = User(username="jane_doe", email="jane@example.com", age=28)

    # Displaying user information
    print(user1)  # Outputs: User(username='john_doe', email='john@example.com', age=30)
    print(user2)  # Outputs: User(username='jane_doe', email='jane@example.com', age=28)

    # Comparing two user instances
    print(user1 == user2)  # Outputs: False

if __name__ == "__main__":
    main()