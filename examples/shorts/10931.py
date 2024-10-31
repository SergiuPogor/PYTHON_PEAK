class CustomContextManager:
    def __enter__(self):
        # Code to set up the resource
        print("Entering the context: resource setup")
        return self  # Returning self to use in the block

    def __exit__(self, exc_type, exc_value, traceback):
        # Code to clean up the resource
        print("Exiting the context: resource cleanup")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True  # Suppress exceptions if desired

def main():
    with CustomContextManager() as resource:
        print("Inside the context: using the resource")
        # Simulate some operation that may fail
        # raise ValueError("Something went wrong!")

if __name__ == "__main__":
    main()