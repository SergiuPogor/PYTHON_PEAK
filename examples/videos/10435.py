import re

def replace_patterns(text, replacements):
    # Replace patterns in text based on the replacements dictionary
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text)
    return text

def main():
    # Example text where we want to replace patterns
    sample_text = "Hello, my name is John. I love Python. Python is great!"
    
    # Patterns to replace
    replacements = {
        r"John": "Jane",            # Replace name
        r"Python": "programming",   # Replace technology
    }
    
    # Perform the replacements
    modified_text = replace_patterns(sample_text, replacements)
    
    # Print the original and modified text
    print(f"Original Text: {sample_text}")
    print(f"Modified Text: {modified_text}")

if __name__ == "__main__":
    main()