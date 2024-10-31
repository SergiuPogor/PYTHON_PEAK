# Function to merge two lists into a dictionary using comprehension
def merge_lists_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

def main():
    # Sample data for merging
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "New York"]

    # Merging lists into a dictionary
    merged_dict = merge_lists_to_dict(keys, values)

    # Displaying the merged dictionary
    print("Merged Dictionary:", merged_dict)

if __name__ == "__main__":
    main()