import re

# Sample strings for demonstration
text1 = "Hello, world!"
text2 = "world! Hello again."

# Using re.match - checks only the start of the string
match_result1 = re.match(r"Hello", text1)  # This will match
match_result2 = re.match(r"world", text1)  # This will not match

# Using re.search - checks the entire string
search_result1 = re.search(r"Hello", text2)  # This will match
search_result2 = re.search(r"world", text2)  # This will also match

# Outputting the results
print(f"Match 1: {match_result1.group() if match_result1 else 'No match'}")  # Output: Hello
print(f"Match 2: {match_result2.group() if match_result2 else 'No match'}")  # Output: No match

print(f"Search 1: {search_result1.group() if search_result1 else 'No match'}")  # Output: Hello
print(f"Search 2: {search_result2.group() if search_result2 else 'No match'}")  # Output: world