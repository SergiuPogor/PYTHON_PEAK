from collections import Counter

# Sample data: a list of items with some duplicates
data = ['apple', 'banana', 'apple', 'orange', 
        'banana', 'banana', 'kiwi', 'kiwi', 'kiwi']

# Count frequencies using collections.Counter
frequency_count = Counter(data)

# Display the results
for item, count in frequency_count.items():
    print(f"{item}: {count}")  # Print item and its frequency