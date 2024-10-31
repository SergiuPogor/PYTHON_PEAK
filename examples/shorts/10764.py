# Singleton metaclass to ensure only one instance of a class
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Singleton class using the SingletonMeta metaclass
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Function to demonstrate Singleton behavior
def singleton_test():
    obj1 = SingletonClass("First Instance")
    obj2 = SingletonClass("Second Instance")

    # Both obj1 and obj2 refer to the same instance
    print(f"Object 1 Value: {obj1.value}")  # Output: First Instance
    print(f"Object 2 Value: {obj2.value}")  # Output: First Instance

# Run the test
singleton_test()