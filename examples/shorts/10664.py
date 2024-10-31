def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Arguments received: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            print("Function executed.")
            return result
        return wrapper
    return decorator

@decorator_with_args("Hello", "World")
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("Alice")