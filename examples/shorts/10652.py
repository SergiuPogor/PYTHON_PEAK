# Safely handle missing keys in nested dictionaries

# Sample nested dictionary
data = {
    "user": {
        "name": "Alice",
        "preferences": {
            "theme": "dark",
            "notifications": None
        }
    },
    "settings": {
        "language": "en"
    }
}

# Using dict.get() to safely access nested values
user_theme = data.get("user", {}).get("preferences", {}).get("theme", "light")
user_notifications = data.get("user", {}).get("preferences", {}).get("notifications", "enabled")

print("User theme:", user_theme)  # Output: dark
print("User notifications:", user_notifications)  # Output: enabled

# Using collections.defaultdict for handling missing keys
from collections import defaultdict

# Create a nested defaultdict
nested_data = defaultdict(lambda: defaultdict(dict))
nested_data["user"]["name"] = "Bob"
nested_data["user"]["preferences"]["theme"] = "light"

# Safely access values with defaultdict
user_theme_default = nested_data["user"]["preferences"]["theme"]
user_language_default = nested_data["user"]["preferences"]["language"]  # Returns empty dict

print("User theme with defaultdict:", user_theme_default)  # Output: light
print("User language with defaultdict:", user_language_default)  # Output: {}