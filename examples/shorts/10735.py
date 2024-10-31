def check_value(value):
    if value is None:
        return "Value is None!"
    elif value is False:
        return "Value is False!"
    else:
        return "Value is something else!"

# Testing the function
print(check_value(None))  # Output: Value is None!
print(check_value(False))  # Output: Value is False!
print(check_value(0))      # Output: Value is something else!
print(check_value(""))     # Output: Value is something else!