import re

def validate_email(email):
    # Simple regex for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def extract_phone_numbers(text):
    # Regex to find phone numbers in the format (xxx) xxx-xxxx or xxx-xxx-xxxx
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def replace_dates(text):
    # Replace dates in MM/DD/YYYY format with YYYY-MM-DD
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    return re.sub(pattern, r'\3-\1-\2', text)

def main():
    email = "example@test.com"
    print(f"Is '{email}' valid? {validate_email(email)}")

    sample_text = "Call me at (123) 456-7890 or 987-654-3210."
    phones = extract_phone_numbers(sample_text)
    print(f"Found phone numbers: {phones}")

    date_text = "Important dates are 12/25/2024 and 01/01/2025."
    new_date_text = replace_dates(date_text)
    print(f"Formatted dates: {new_date_text}")

if __name__ == "__main__":
    main()