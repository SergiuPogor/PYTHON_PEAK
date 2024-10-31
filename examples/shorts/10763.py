import re

# Sample text to demonstrate complex string replacement
text = "The price of apples is $5.00, bananas are $2.50, and oranges cost $3.00."

# Function to replace currency values with a different format
def format_prices(input_text):
    # Replace dollar amounts with a formatted string
    return re.sub(r'\$(\d+\.\d{2})', r'Price: \1 USD', input_text)

# Another use case: clean up and standardize phone numbers
def standardize_phone_numbers(input_text):
    # Find phone numbers in various formats and standardize them
    return re.sub(r'(\d{3})[.-]?(\d{3})[.-]?(\d{4})', r'(\1) \2-\3', input_text)

# Example text with phone numbers
text_with_numbers = "Call me at 123-456-7890 or 987.654.3210."

# Format prices and standardize phone numbers
formatted_prices = format_prices(text)
standardized_numbers = standardize_phone_numbers(text_with_numbers)

print(formatted_prices)  # Output: The price of apples is Price: 5.00 USD, bananas are Price: 2.50 USD, and oranges cost Price: 3.00 USD.
print(standardized_numbers)  # Output: Call me at (123) 456-7890 or (987) 654-3210.