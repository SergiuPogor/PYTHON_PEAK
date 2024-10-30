# Example: Using closures to create a custom counter with nested functions

def counter(start=0):
    count = start  # Initial state captured by the nested function

    def increment():
        nonlocal count  # Allows modification of 'count' from the enclosing scope
        count += 1
        return count

    return increment

# Usage of the counter closure
counter_a = counter(10)  # Starts at 10
counter_b = counter(50)  # Independent counter starting at 50

print(counter_a())  # Output: 11
print(counter_a())  # Output: 12
print(counter_b())  # Output: 51
print(counter_b())  # Output: 52

# Another example: A configuration generator using closures

def config_generator(option):
    # Base configuration capturing 'option' for the nested functions
    def apply_config(value):
        return f"Config with {option}: {value * 2}"

    return apply_config

configA = config_generator("Speed")
configB = config_generator("Memory")

print(configA(5))  # Output: "Config with Speed: 10"
print(configB(3))  # Output: "Config with Memory: 6"