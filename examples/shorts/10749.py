from collections import defaultdict

# Using a nested dictionary
data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Wonderland",
            "zip": None
        }
    }
}

# Accessing nested keys with error handling
def get_user_city(user_data):
    # Using get() to avoid KeyError
    return user_data.get("address", {}).get("city", "Unknown City")

# Using defaultdict for automatic default values
def create_user_data():
    user_data = defaultdict(lambda: {"name": "Unknown", "address": {"city": "Unknown", "zip": "00000"}})
    user_data["Bob"]["name"] = "Bob"
    return user_data

def main():
    print("User city:", get_user_city(data["user"]))
    
    # Demonstrate defaultdict
    user_data = create_user_data()
    print("Default user data for Charlie:", user_data["Charlie"])

if __name__ == "__main__":
    main()