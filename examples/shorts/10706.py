import shutil

def print_formatted_output(data):
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns

    # Print header
    print("=" * width)
    print("Data Output".center(width))
    print("=" * width)

    # Print each item in data with formatting
    for item in data:
        print(str(item).ljust(width))

    print("=" * width)

def main():
    # Sample data for demonstration
    sample_data = [
        "Item 1: Learn Python Basics",
        "Item 2: Understand Data Structures",
        "Item 3: Explore Python Libraries",
        "Item 4: Build Real Projects",
        "Item 5: Contribute to Open Source"
    ]
    print_formatted_output(sample_data)

if __name__ == "__main__":
    main()