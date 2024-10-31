class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

def main():
    instance1 = SingletonClass()
    instance2 = SingletonClass()

    print(f"Instance 1 value: {instance1.increment()}")  # Output: 1
    print(f"Instance 2 value: {instance2.increment()}")  # Output: 2

    print(f"Are both instances the same? {instance1 is instance2}")  # Output: True

if __name__ == "__main__":
    main()