# module_a.py
def greet():
    print("Hello from Module A!")

# Avoid circular import by importing locally
def call_module_b():
    from module_b import farewell  # Local import to avoid circular import
    farewell()

# module_b.py
def farewell():
    print("Goodbye from Module B!")

# Main script
if __name__ == "__main__":
    from module_a import greet
    greet()
    call_module_b()  # Calls Module B's farewell function