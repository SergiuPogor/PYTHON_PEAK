def update_variables(var_name, new_value):
    # Simulating a situation where variable names are dynamic
    a = 10
    b = 20
    c = 30
    
    # Update the variable using locals()
    if var_name in locals():
        locals()[var_name] = new_value
    else:
        raise ValueError(f"Variable '{var_name}' not found.")

    return locals()

# Usage example
if __name__ == '__main__':
    print("Initial values:")
    print(update_variables('a', 100))  # Update variable 'a' to 100
    print(update_variables('b', 200))  # Update variable 'b' to 200
    print(update_variables('c', 300))  # Update variable 'c' to 300

    # This will raise an error since 'd' does not exist
    try:
        print(update_variables('d', 400))
    except ValueError as e:
        print(e)  # Variable 'd' not found.