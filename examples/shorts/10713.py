# Example: Safely merging multiple dictionaries with Python's `|=` operator

# Dictionary for main application config
app_config = {
    "debug": True,
    "theme": "dark",
    "max_connections": 10,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

# Additional settings coming from a user profile
user_settings = {
    "theme": "light",
    "font_size": "large",
    "database": {
        "host": "remote_host",
        "backup": True
    }
}

# Another config that could be loaded from a file or external API
feature_toggles = {
    "enable_feature_x": True,
    "debug": False
}

# Safely combine configurations without losing data
# app_config |= user_settings will not overwrite the existing values in app_config
merged_config = {**app_config, **user_settings, **feature_toggles}

# Display merged configurations
print("Combined Configuration:", merged_config)

# Handle nested dictionaries with manual control for complex cases
# Custom merge of `app_config` and `user_settings` to handle 'database' nested dictionary
merged_config = {
    **app_config,
    **user_settings,
    **feature_toggles,
    "database": {**app_config["database"], **user_settings["database"]}
}

print("Final Merged Config with Nested Database Settings:", merged_config)