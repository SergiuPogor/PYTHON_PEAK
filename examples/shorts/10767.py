import re

# Function to dynamically transform matched patterns
def dynamic_replacement(match):
    # Get the matched string
    matched_text = match.group()
    
    # Example transformation: Capitalize the matched word
    return matched_text.upper()

# Sample text with words to replace
text = "Hello world! This is a test. Python is fun."

# Use re.sub with the dynamic_replacement function
result = re.sub(r'\b\w+\b', dynamic_replacement, text)

# Print the result
print("Original Text:", text)
print("Transformed Text:", result)