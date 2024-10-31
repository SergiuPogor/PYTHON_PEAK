# Example: Using re.escape to handle strings with special characters in regex searches

import re

# Define a user-provided input string with special regex characters
user_input = "price is $9.99 (on sale now!) for #100* items."

# Escape special characters in the input string for a safe regex search
escaped_input = re.escape(user_input)

# Example 1: Find escaped pattern in a paragraph of text
text = "Our latest promotion says price is $9.99 (on sale now!) for #100* items. Limited offer!"
match = re.search(escaped_input, text)

# Output match status
if match:
    print("Match found at position:", match.start())
else:
    print("No match found.")

# Example 2: Dynamic regex using re.escape for specific words in a query list
query_keywords = ["$pecial_offer", "savings+", "#top-rated"]
escaped_keywords = [re.escape(word) for word in query_keywords]

# Join escaped keywords into a regex pattern
pattern = "|".join(escaped_keywords)

# Test pattern against a target string
target_text = "Our $pecial_offer ends soon. Check top-rated items or find big savings+ right now!"
matches = re.findall(pattern, target_text)

# Output matched words
print("Keywords found:", matches)