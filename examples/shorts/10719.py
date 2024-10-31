from dataclasses import dataclass, field
from typing import List, Dict

# Define a dataclass for tracking settings, avoiding shared mutable defaults
@dataclass
class UserSettings:
    username: str
    preferences: List[str] = field(default_factory=lambda: ["dark mode", "notifications"])
    config: Dict[str, int] = field(default_factory=lambda: {"volume": 50, "brightness": 70})

# Create multiple instances and show they do not share mutable defaults
user1 = UserSettings(username="Alice")
user2 = UserSettings(username="Bob")

# Modify preferences and config for user1
user1.preferences.append("auto-update")
user1.config["volume"] = 80

# Check that user2's preferences and config are unaffected by user1's changes
print(f"User1 Preferences: {user1.preferences}")  # Output: ["dark mode", "notifications", "auto-update"]
print(f"User2 Preferences: {user2.preferences}")  # Output: ["dark mode", "notifications"]

print(f"User1 Config: {user1.config}")            # Output: {"volume": 80, "brightness": 70}
print(f"User2 Config: {user2.config}")            # Output: {"volume": 50, "brightness": 70}

# Additional usage of mutable defaults with field(default_factory=...) for dynamic instance-specific behavior
default_log_path = field(default_factory=lambda: f"/logs/{UserSettings.username}.log")