from dataclasses import dataclass, field

@dataclass
class UserProfile:
    username: str
    email: str
    _token: str = field(init=False)  # Prevent initialization

    def __post_init__(self):
        # Generate a token after initialization
        self._token = self.generate_token()

    def generate_token(self):
        # Simulate token generation
        return f"{self.username}-token"

# Example usage
user = UserProfile(username="alice", email="alice@example.com")
print(f"Username: {user.username}")
print(f"Email: {user.email}")
print(f"Token: {user._token}")  # Token is set after initialization