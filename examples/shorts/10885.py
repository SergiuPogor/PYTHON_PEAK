def convert_lists_to_dict(keys, values):
    """Convert two lists into a dictionary."""
    return dict(zip(keys, values))

def main():
    keys = ['name', 'age', 'city']
    values = ['Alice', 30, 'New York']

    # Convert lists to dictionary
    result_dict = convert_lists_to_dict(keys, values)
    print("Resulting Dictionary:", result_dict)

if __name__ == "__main__":
    main()