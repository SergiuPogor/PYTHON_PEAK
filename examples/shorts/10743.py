from dataclasses import dataclass, astuple

@dataclass
class User:
    name: str
    age: int
    email: str

# Function to demonstrate the use of astuple
def main():
    user = User(name="Alice", age=30, email="alice@example.com")

    # Convert the data class to a tuple
    user_tuple = astuple(user)
    
    # Accessing tuple elements
    print("User Tuple:", user_tuple)         # Output: User Tuple: ('Alice', 30, 'alice@example.com')
    print("Name:", user_tuple[0])            # Output: Name: Alice
    print("Age:", user_tuple[1])             # Output: Age: 30
    print("Email:", user_tuple[2])           # Output: Email: alice@example.com

if __name__ == "__main__":
    main()  # Execute the main function