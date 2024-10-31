import re

# Sample text containing overlapping patterns
text = "ababababab"

# Regular expression pattern to find 'abab'
pattern = r'abab'

# Using re.finditer to match overlapping patterns
matches = [match.span() for match in re.finditer(pattern, text)]

# Displaying results
print("Overlapping Matches:")
for start, end in matches:
    print(f"Match found at index: {start}-{end}")

# Adjusting the search position to find more overlaps
# Shift start position for the next search
overlaps = []
start_position = 0

while True:
    match = re.search(pattern, text[start_position:])
    if not match:
        break
    start_index = match.start() + start_position
    overlaps.append((start_index, start_index + len(pattern)))
    start_position += match.start() + 1  # Shift position for overlap

print("Detailed Overlapping Matches:")
for start, end in overlaps:
    print(f"Match found at index: {start}-{end}")