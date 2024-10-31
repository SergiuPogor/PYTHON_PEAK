class BaseClass:
    def greet(self):
        return "Hello from BaseClass!"

def custom_greet(self):
    return "Hello from the dynamically overridden method!"

# Example usage
if __name__ == "__main__":
    obj = BaseClass()
    print(obj.greet())  # Original greeting

    # Dynamically override the greet method
    BaseClass.greet = custom_greet

    print(obj.greet())  # New greeting from the overridden method