from collections import Counter

def count_frequencies(data):
    # Count frequencies using collections.Counter
    frequency_count = Counter(data)
    return frequency_count

def main():
    # Sample data: list of items
    items = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
    # Count the frequencies of each item
    result = count_frequencies(items)
    
    print("Frequency Count:")
    for item, count in result.items():
        print(f"{item}: {count}")

if __name__ == "__main__":
    main()