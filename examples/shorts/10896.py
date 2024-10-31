class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example usage
if __name__ == "__main__":
    obj1 = SingletonClass("First Instance")
    obj2 = SingletonClass("Second Instance")

    print("Value of obj1:", obj1.value)  # Output: First Instance
    print("Value of obj2:", obj2.value)  # Output: First Instance
    print("Are both instances the same?", obj1 is obj2)  # Output: True