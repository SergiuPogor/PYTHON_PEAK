# Example of context-dependent function implementation using decorators

from functools import wraps

# Decorator to modify function behavior based on context
def context_dependent(func):
    @wraps(func)
    def wrapper(*args, context=None, **kwargs):
        if context == 'special':
            return func(*args, **kwargs) + " - Context: Special"
        return func(*args, **kwargs) + " - Context: Normal"
    return wrapper

@context_dependent
def greet(name):
    return f"Hello, {name}!"

# Using the function with different contexts
normal_greeting = greet("Alice")
special_greeting = greet("Bob", context='special')

print(normal_greeting)  # Output: Hello, Alice! - Context: Normal
print(special_greeting)  # Output: Hello, Bob! - Context: Special

# Example 2: A more complex scenario using the context to modify behavior
@context_dependent
def calculate(value, operation):
    if operation == 'double':
        return value * 2
    return value

# Different contexts for calculations
double_context = calculate(5, 'double', context='special')
normal_context = calculate(5, 'normal')

print(double_context)  # Output: 5 - Context: Special
print(normal_context)  # Output: 5 - Context: Normal