from collections import defaultdict

# Function to count occurrences of items in a list
def count_items(items):
    # Create a defaultdict with int as the default factory
    count_dict = defaultdict(int)
    
    # Count each item in the list
    for item in items:
        count_dict[item] += 1
    
    return count_dict

# Example of using the count_items function
if __name__ == "__main__":
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    
    # Count occurrences of each item
    counted_items = count_items(sample_data)
    
    # Print the results
    for item, count in counted_items.items():
        print(f"{item}: {count}")  # Output each item with its count