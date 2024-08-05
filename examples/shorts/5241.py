class MyClass:
    def __call__(self, x):
        return x * 2

def my_function(y):
    return y + 5

def execute_if_callable(obj, value):
    if callable(obj):
        return obj(value)
    else:
        return "Object is not callable"

# Create instances
my_instance = MyClass()
result1 = execute_if_callable(my_instance, 10)
result2 = execute_if_callable(my_function, 10)
result3 = execute_if_callable(123, 10)

print(f"Result of my_instance: {result1}")  # Should print 20
print(f"Result of my_function: {result2}")  # Should print 15
print(f"Result of a non-callable object: {result3}")  # Should print "Object is not callable"

# Example with a list of mixed callables and non-callables
objects = [my_instance, my_function, 123, "string"]

# Using callable to filter and execute callables only
for obj in objects:
    if callable(obj):
        print(f"{obj} is callable, result: {obj(10)}")
    else:
        print(f"{obj} is not callable")
