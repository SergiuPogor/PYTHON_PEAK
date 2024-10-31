import sys

# List of repeated strings to demonstrate sys.intern
strings = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Interning the strings
interned_strings = [sys.intern(s) for s in strings]

# Check memory addresses to see if interning worked
unique_strings = set(interned_strings)
print(f"Unique strings: {unique_strings}")

# Compare memory addresses of repeated strings
for s in unique_strings:
    print(f"String: {s}, ID: {id(s)}")

# Result:
# This will show that 'apple' and 'banana' have the same ID when interned.
# Demonstrates that sys.intern saves memory by ensuring only one copy
# of each unique string exists in memory.