# Pythonic trick: Using `zip()` for parallel iteration and data processing
# Example 1: Merging two lists of data cleanly
users = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for user, score in zip(users, scores):
    print(f"User: {user} - Score: {score}")

# Example 2: Iterating over multiple lists, useful in real applications for parallel data processing
dates = ["2023-10-01", "2023-10-02", "2023-10-03"]
login_counts = [12, 17, 5]
messages_sent = [8, 15, 4]

for date, logins, messages in zip(dates, login_counts, messages_sent):
    print(f"Date: {date} - Logins: {logins}, Messages Sent: {messages}")

# Example 3: Pairing data from two files for comparison, such as logs or configuration details
with open('/tmp/test/input.txt', 'r') as file1, open('/tmp/test/input.zip', 'r') as file2:
    for line1, line2 in zip(file1, file2):
        print(f"File1: {line1.strip()} | File2: {line2.strip()}")

# Example 4: Efficient way to handle dictionary key-value updates across multiple dictionaries
defaults = {"color": "blue", "size": "M"}
user_config = {"size": "L", "theme": "dark"}

merged_config = {key: user_config.get(key, defaults[key]) for key in defaults.keys()}
print("Merged configuration:", merged_config)

# Example 5: Creating a dictionary from two lists, useful for quick data structure creation
keys = ["name", "age", "location"]
values = ["Eve", 29, "New York"]

user_profile = dict(zip(keys, values))
print("User Profile:", user_profile)