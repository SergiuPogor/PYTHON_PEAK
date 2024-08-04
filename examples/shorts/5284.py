# Practical use of frozenset() in a real-world scenario

# Example: Creating immutable sets to use as dictionary keys

permissions = {
    frozenset(["read", "write"]): "Editor",
    frozenset(["read"]): "Viewer"
}

user_permissions = ["read", "write"]
role = permissions.get(frozenset(user_permissions), "Unknown")
print(f"User role: {role}")

# Example: Using frozenset() to ensure data immutability

unique_ids = frozenset([101, 102, 103, 104])
print(f"Unique IDs: {unique_ids}")

try:
    unique_ids.add(105)
except AttributeError as e:
    print(f"Error: {e}")

# Example: Checking membership in immutable sets

valid_colors = frozenset(["red", "green", "blue"])
color = "red"
if color in valid_colors:
    print(f"{color} is a valid color.")
else:
    print(f"{color} is not a valid color.")

# Example: Using frozenset() to remove duplicates and ensure immutability

data = ["apple", "banana", "apple", "orange"]
unique_data = frozenset(data)
print(f"Unique data: {unique_data}")