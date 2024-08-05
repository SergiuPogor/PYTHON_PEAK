# Example of using chr() to convert integers to Unicode characters

def create_char_string(start, end):
    return ''.join(chr(i) for i in range(start, end + 1))

# Generate a string of characters from ASCII values 65 to 90 (A to Z)
uppercase_alphabet = create_char_string(65, 90)
print(f"Uppercase Alphabet: {uppercase_alphabet}")

# Generate a string of characters from ASCII values 97 to 122 (a to z)
lowercase_alphabet = create_char_string(97, 122)
print(f"Lowercase Alphabet: {lowercase_alphabet}")

# Generate a string of special characters from ASCII values 33 to 47 (!"#$%&'()*+,-./)
special_characters = create_char_string(33, 47)
print(f"Special Characters: {special_characters}")

# Example with Unicode characters beyond ASCII range
# Generate a string of characters from Unicode values 945 to 969 (Greek lowercase letters α to ω)
greek_lowercase = create_char_string(945, 969)
print(f"Greek Lowercase Letters: {greek_lowercase}")

# Checking specific characters
value = 100
character = chr(value)
print(f"Character for integer {value}: {character}")

value = 8364  # Unicode for Euro sign (€)
character = chr(value)
print(f"Character for integer {value}: {character}")

# Using chr() to dynamically create characters based on user input
user_input = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
user_message = ''.join(chr(i) for i in user_input)
print(f"User Message: {user_message}")
