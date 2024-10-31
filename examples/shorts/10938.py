def outer_function(msg):
    # This is the outer function
    def inner_function():
        # This inner function has access to the outer scope
        print(msg)
    return inner_function  # Return the inner function

# Create a closure with a specific message
greet = outer_function("Hello, World!")

# Call the closure
greet()  # Outputs: Hello, World!

# Another example with different message
farewell = outer_function("Goodbye, World!")
farewell()  # Outputs: Goodbye, World!

# Closure can capture and remember different values
def counter(start=0):
    count = [start]  # Mutable state

    def increment():
        count[0] += 1  # Modify the mutable state
        return count[0]
    
    return increment

# Create a counter function starting at 5
my_counter = counter(5)

print(my_counter())  # Outputs: 6
print(my_counter())  # Outputs: 7