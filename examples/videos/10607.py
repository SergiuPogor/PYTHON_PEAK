class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


if __name__ == "__main__":
    s1 = Singleton("First Instance")
    print(f"Value from s1: {s1.get_value()}")  # Should print: First Instance

    s2 = Singleton("Second Instance")
    print(f"Value from s2: {s2.get_value()}")  # Should print: First Instance, not Second Instance

    s1.set_value("Updated Value")
    print(f"Value from s2 after update: {s2.get_value()}")  # Should print: Updated Value

    print(f"Are both instances the same? {s1 is s2}")  # Should print: True