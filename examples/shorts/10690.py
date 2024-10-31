class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        # Initialize only if no instance has been created
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

# Example usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

# Both instances will point to the same object
print(singleton1.value)  # Outputs: 10
print(singleton2.value)  # Outputs: 10

# Check if both instances are the same
print(singleton1 is singleton2)  # Outputs: True