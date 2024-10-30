import re

# Function to perform dynamic replacements based on match content
def dynamic_replacer(match):
    # Extract the matched text
    matched_text = match.group(0)
    # Modify the matched text as needed (example: reversing the match)
    return matched_text[::-1]

def replace_text(input_string):
    # Define a regex pattern to match words
    pattern = r'\b\w+\b'
    
    # Use re.sub with the dynamic_replacer function
    result = re.sub(pattern, dynamic_replacer, input_string)
    
    return result

# Sample input string
input_string = "Hello World! This is a Python tutorial on regex."
# Perform the replacement
output = replace_text(input_string)

# Print the output
print("Original String:", input_string)
print("Modified String:", output)

# Example of using dynamic replacement in a configuration context
def apply_settings(settings):
    # Define a regex pattern to find configuration options
    pattern = r'(\w+): (\w+)'
    
    def setting_replacer(match):
        key, value = match.groups()
        # Modify value based on some conditions
        return f"{key}: {value.upper()}"  # Example transformation

    # Join settings into a single string for processing
    settings_string = "\n".join(f"{key}: {value}" for key, value in settings.items())
    
    # Apply dynamic replacements using re.sub
    modified_settings = re.sub(pattern, setting_replacer, settings_string)
    
    return modified_settings

# Sample settings dictionary
settings = {
    'timeout': '30',
    'max_retries': '5',
    'enable_logging': 'true'
}

# Apply dynamic replacements on settings
updated_settings = apply_settings(settings)

# Print the updated settings
print("\nUpdated Settings:\n", updated_settings)