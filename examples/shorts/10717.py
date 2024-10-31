# Using any() and all() to simplify condition checking in Python

# List of conditions to check, e.g., for validating user input fields
conditions = [user.is_active, user.has_permission, user.email_verified]

# Check if *any* condition is True (ideal for checking minimum requirements)
if any(conditions):
    print("User meets at least one condition. Partial access granted.")

# Check if *all* conditions are True (ideal for full validation)
if all(conditions):
    print("User meets all conditions. Full access granted.")

# Real-world use case: Checking if any file in a list exists in a directory
import os

file_paths = ['/tmp/test/input.txt', '/tmp/test/config.ini', '/tmp/test/data.csv']
if any(os.path.isfile(path) for path in file_paths):
    print("At least one required file is available.")

# Another use case: Validating a list of settings with all()
settings = {"dark_mode": True, "notifications": True, "auto_sync": True}
if all(settings.values()):
    print("All settings are enabled.")

# Using any() to check for any empty values in a data list
data = ["username", "password", ""]
if any(not field for field in data):
    print("Some fields are missing data.")