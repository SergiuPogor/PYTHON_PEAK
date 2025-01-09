from collections import ChainMap

# Example use case: User preferences layered with system defaults
default_config = {'theme': 'light', 'notifications': True, 'language': 'en'}
user_config = {'theme': 'dark', 'notifications': False}

config = ChainMap(user_config, default_config)

# Access configuration with ChainMap - shows merged but separate dictionaries
print("Effective configuration:", dict(config))
print("User preference for theme:", config['theme'])
print("System default for language:", config['language'])

# Modifying user preferences reflects immediately in ChainMap
user_config['language'] = 'es'
print("Updated configuration with new language preference:", dict(config))

# Nested settings scenario: Global, department, and user-level configs
global_config = {'storage_limit': '100GB', 'backup': True, 'retention': '30 days'}
department_config = {'storage_limit': '200GB', 'retention': '15 days'}
user_specific_config = {'storage_limit': '50GB'}

layered_config = ChainMap(user_specific_config, department_config, global_config)

print("\nLayered configuration for storage limit:", layered_config['storage_limit'])
print("Retention policy (from department):", layered_config['retention'])

# Using ChainMap to update or add settings without modifying originals
updated_config = layered_config.new_child({'backup': False})
print("\nTemporary updated configuration:", dict(updated_config))

# Verify original configurations remain unchanged
print("Original user-specific configuration:", user_specific_config)
print("Original department configuration:", department_config)
print("Original global configuration:", global_config)

# Example for handling dynamic defaults and environment-based settings
import os
environment_settings = {'database': 'prod_db', 'debug': False}
os.environ['APP_MODE'] = 'development'

# Dynamic default setup: switches between configs based on environment
env_defaults = {'database': 'test_db', 'debug': True} if os.environ.get('APP_MODE') == 'development' else environment_settings

config_chain = ChainMap(env_defaults, environment_settings)

print("\nDynamic configuration based on environment:", dict(config_chain))
print("Current debug setting:", config_chain['debug'])