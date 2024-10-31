from dataclasses import dataclass, replace

@dataclass
class UserProfile:
    username: str
    email: str
    age: int

# Original user profile
user1 = UserProfile(username="john_doe", email="john@example.com", age=30)

# Create a new user profile with a modified email
user2 = replace(user1, email="john.new@example.com")

# Display both profiles
print(f'Original Profile: {user1}')  # Output: Original Profile: UserProfile(username='john_doe', email='john@example.com', age=30)
print(f'Updated Profile: {user2}')    # Output: Updated Profile: UserProfile(username='john_doe', email='john.new@example.com', age=30)

# Show that the original profile remains unchanged
print(f'Original Email: {user1.email}')  # Output: Original Email: john@example.com
print(f'Updated Email: {user2.email}')    # Output: Updated Email: john.new@example.com