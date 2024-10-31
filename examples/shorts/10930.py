from functools import wraps

def repeat(num_times: int):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name: str) -> str:
    return f"Hello, {name}!"

def main():
    print(greet("Alice"))

if __name__ == "__main__":
    main()