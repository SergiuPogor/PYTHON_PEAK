from functools import wraps

def my_decorator(arg1, arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Arguments passed to decorator: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@my_decorator("Hello", "World")
def greet(name):
    """This function greets a person."""
    return f"{name}, welcome to Python!"

@my_decorator(42, 3.14)
def calculate_area(radius):
    """Calculates the area of a circle."""
    return 3.14 * (radius ** 2)

if __name__ == "__main__":
    print(greet("Alice"))
    print("Area:", calculate_area(5))
    print("Function name:", greet.__name__)
    print("Function docstring:", greet.__doc__)