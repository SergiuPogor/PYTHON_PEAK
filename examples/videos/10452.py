import re

def is_valid_email(email):
    """Check if the email is valid using regex."""
    # Basic regex pattern for validating an email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Match the email with the regex pattern
    if re.match(pattern, email):
        domain = email.split('@')[1]
        return check_domain(domain)
    
    return False

def check_domain(domain):
    """Check if the domain exists (simulated)."""
    # Here we would normally check the domain against a list or a DNS query
    valid_domains = ['example.com', 'test.com', 'mydomain.org']
    return domain in valid_domains

# Example usage
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "user@invalid-domain",
        "user@test.com",
        "user@fake.com"
    ]

    for email in test_emails:
        if is_valid_email(email):
            print(f"{email} is valid.")
        else:
            print(f"{email} is invalid.")