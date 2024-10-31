# Example of using dict.get() in nested dictionaries

data = {
    "user": {
        "name": "Alice",
        "age": 30,
        "preferences": {
            "language": "Python",
            "theme": "dark"
        }
    },
    "settings": {
        "notifications": {
            "email": True,
            "sms": False
        }
    }
}

# Accessing values safely using dict.get()
language = data.get("user", {}).get("preferences", {}).get("language", "English")
email_notifications = data.get("settings", {}).get("notifications", {}).get("email", False)

print(f"User Language: {language}")  # Output: User Language: Python
print(f"Email Notifications: {email_notifications}")  # Output: Email Notifications: True

# Trying to access a non-existing key with a default value
favorite_color = data.get("user", {}).get("preferences", {}).get("color", "Not specified")
print(f"Favorite Color: {favorite_color}")  # Output: Favorite Color: Not specified