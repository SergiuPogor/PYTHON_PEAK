import copyreg
import pickle

# Define a simple class
class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Custom serialization function
def serialize_custom_object(obj):
    return (obj.name, obj.value)

# Custom deserialization function
def deserialize_custom_object(name, value):
    return CustomObject(name, value)

# Registering the serialization functions
copyreg.pickle(CustomObject, serialize_custom_object,
                deserialize_custom_object)

def save_custom_object(obj, filename):
    """Save a custom object to a file."""
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def load_custom_object(filename):
    """Load a custom object from a file."""
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    obj = CustomObject("example", 42)
    filename = '/tmp/test/custom_object.pkl'
    
    # Save the object
    save_custom_object(obj, filename)
    
    # Load the object
    loaded_obj = load_custom_object(filename)
    print(f"Loaded object: Name: {loaded_obj.name}, Value: {loaded_obj.value}")

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()