def dynamic_variable_access(config_name):
    config_user = "admin_user"
    config_password = "secure_pass"
    config_timeout = 300

    # Use locals() to access variable dynamically based on config_name
    try:
        # Access local variable by its name in a dynamic way
        config_value = locals().get(config_name)
        
        # Simulate a real-world check (like API configurations)
        if config_value is None:
            raise ValueError(f"Configuration '{config_name}' not found!")
        
        print(f"Value for '{config_name}': {config_value}")
    except ValueError as e:
        print(e)

# Testing dynamic access with various config names
dynamic_variable_access("config_user")       # Output: Value for 'config_user': admin_user
dynamic_variable_access("config_password")   # Output: Value for 'config_password': secure_pass
dynamic_variable_access("config_timeout")    # Output: Value for 'config_timeout': 300
dynamic_variable_access("config_retry")      # Output: Configuration 'config_retry' not found!