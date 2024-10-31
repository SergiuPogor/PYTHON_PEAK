import pickle

# Define a sample Python object (dictionary)
data = {
    'name': 'Alice',
    'age': 30,
    'skills': ['Python', 'Machine Learning', 'Data Analysis']
}

# Serialize the object to a file using pickle
with open('/tmp/test/data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize the object from the file
with open('/tmp/test/data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Display the loaded data
print("Loaded Data:", loaded_data)

# Example with a custom class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of User
user_instance = User("Bob", 25)

# Serialize the User object
with open('/tmp/test/user.pkl', 'wb') as file:
    pickle.dump(user_instance, file)

# Deserialize the User object
with open('/tmp/test/user.pkl', 'rb') as file:
    loaded_user = pickle.load(file)

# Display the loaded User object
print("Loaded User:", loaded_user.name, loaded_user.age)