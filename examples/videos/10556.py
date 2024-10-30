import weakref

class User:
    def __init__(self, name):
        self.name = name

# Creating a WeakSet to hold User instances
user_set = weakref.WeakSet()

# Adding User instances to the WeakSet
user1 = User("Alice")
user2 = User("Bob")
user_set.add(user1)
user_set.add(user2)

# Displaying current users in the WeakSet
print("Current users in the WeakSet:")
for user in user_set:
    print(user.name)

# Deleting a strong reference to user1
del user1

# At this point, user1 should be removed from the WeakSet
print("Users in the WeakSet after deleting user1:")
for user in user_set:
    print(user.name)

# Creating a function to demonstrate memory efficiency
def create_users(num):
    for i in range(num):
        user_set.add(User(f"User-{i}"))

# Creating multiple users
create_users(10)

# Displaying the remaining users in the WeakSet
print("Remaining users in the WeakSet:")
for user in user_set:
    print(user.name)