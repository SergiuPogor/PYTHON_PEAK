from dataclasses import dataclass, replace

@dataclass(frozen=True)
class UserProfile:
    username: str
    age: int
    hobbies: list

# Create an original user profile
original_profile = UserProfile("bob", 25, ["gaming", "reading"])

# Use dataclasses.replace to create a new instance
# with a modified age and a new hobby
updated_profile = replace(original_profile, age=26, hobbies=["gaming", "reading", "swimming"])

# Display the original and updated profiles
print(f"Original Profile: {original_profile}")
print(f"Updated Profile: {updated_profile}")

# Confirm that the original is unchanged
assert original_profile.age == 25
assert original_profile.hobbies == ["gaming", "reading"]

# Working with a list of user profiles
profiles = [
    UserProfile("alice", 30, ["hiking"]),
    UserProfile("charlie", 28, ["cooking", "biking"])
]

# Update profiles using replace in a loop
updated_profiles = [
    replace(profile, hobbies=profile.hobbies + ["traveling"]) for profile in profiles
]

# Display the updated list of profiles
for profile in updated_profiles:
    print(profile)