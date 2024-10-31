# Example of using setdefault in a dictionary
data = {
    "users": {}
}

# Adding user preferences with setdefault
user = "alice"
preference = data["users"].setdefault(user, {"theme": "light", "language": "en"})

# Updating the user preferences
preference["language"] = "fr"

# Adding another user
user = "bob"
data["users"].setdefault(user, {"theme": "dark", "language": "en"})

# Display the current users and their preferences
for user, prefs in data["users"].items():
    print(f"User: {user}, Preferences: {prefs}")

# Output:
# User: alice, Preferences: {'theme': 'light', 'language': 'fr'}
# User: bob, Preferences: {'theme': 'dark', 'language': 'en'}

# Using setdefault in a nested dictionary scenario
nested_data = {}

# Incrementing counts of items in nested dictionaries
items = ["apple", "banana", "apple", "orange", "banana"]

for item in items:
    nested_data.setdefault(item, 0)  # Initialize key with 0 if not present
    nested_data[item] += 1  # Increment the count

# Display the item counts
print(nested_data)

# Output:
# {'apple': 2, 'banana': 2, 'orange': 1}