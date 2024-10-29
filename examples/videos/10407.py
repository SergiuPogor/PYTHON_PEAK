import weakref

class ClosureExample:
    def __init__(self, value):
        self.value = value

    def make_closure(self):
        # Using a weak reference to avoid memory leak
        def closure():
            return weakref.ref(self.value)()
        return closure

def main():
    # Create an instance of ClosureExample
    example = ClosureExample("I am a closure!")

    # Create a closure function
    closure_func = example.make_closure()

    print("Closure output:", closure_func())

    # Example of deleting the outer variable
    del example

    # Attempting to call the closure after deleting the outer variable
    print("After deleting example:", closure_func())

if __name__ == "__main__":
    main()