import weakref

class LargeObject:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

# Function to demonstrate weak references
def weak_ref_demo():
    large_obj = LargeObject("Big Data")
    weak_obj = weakref.ref(large_obj)  # Create a weak reference

    print(f"Weak reference points to: {weak_obj()}")
    
    # Delete the strong reference
    del large_obj
    print(f"After deletion, weak reference points to: {weak_obj()}")

# Run the demonstration
weak_ref_demo()