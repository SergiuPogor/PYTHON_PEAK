# Example of using globals() to dynamically access and modify global variables

# Define some global variables
global_var1 = "Initial value"
global_var2 = 42

def modify_globals():
    # Access global variables using globals()
    global_vars = globals()
    
    # Print current values
    print(f"Before modification: {global_var1}, {global_var2}")
    
    # Modify global variables dynamically
    global_vars['global_var1'] = "Modified value"
    global_vars['global_var2'] = 100
    
    # Print modified values
    print(f"After modification: {global_var1}, {global_var2}")

# Call the function
modify_globals()

# Access global variables directly to see the effect
print(f"Direct access after modification: {global_var1}, {global_var2}")