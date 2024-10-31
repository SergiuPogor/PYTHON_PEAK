class CallableObject:
    def __init__(self, name):
        self.name = name

    def __call__(self, greeting):
        return f"{greeting}, {self.name}!"

# Usage example
if __name__ == "__main__":
    obj = CallableObject("Alice")
    print(obj("Hello"))  # Output: Hello, Alice!