from dataclasses import dataclass, replace

@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str

# Original user instance
original_user = User(name="Alice", age=30, email="alice@example.com")

# Create a new instance with a modified email
updated_user = replace(original_user, email="alice_new@example.com")

# Show the original and updated user details
print("Original User:", original_user)
print("Updated User:", updated_user)

# This demonstrates immutability in action:
# original_user remains unchanged while updated_user reflects the new email