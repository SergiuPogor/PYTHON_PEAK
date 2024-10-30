from dataclasses import dataclass, field
from typing import List

@dataclass
class UserProfile:
    username: str
    preferences: List[str] = field(default_factory=list)

def create_user_profiles(usernames):
    user_profiles = []
    for username in usernames:
        # Each profile gets a fresh list for preferences
        profile = UserProfile(username)
        user_profiles.append(profile)
    return user_profiles

def add_preference(profiles, username, preference):
    for profile in profiles:
        if profile.username == username:
            profile.preferences.append(preference)

# Example usage
usernames = ['alice', 'bob', 'charlie']
profiles = create_user_profiles(usernames)

add_preference(profiles, 'alice', 'dark mode')
add_preference(profiles, 'bob', 'notifications on')
add_preference(profiles, 'charlie', 'newsletter subscribed')

for profile in profiles:
    print(f"{profile.username}: {profile.preferences}")