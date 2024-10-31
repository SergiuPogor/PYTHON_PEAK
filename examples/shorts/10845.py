from collections import Counter

def count_frequencies(data):
    return Counter(data)

def main():
    # Example data: list of fruits
    fruits = ["apple", "banana", "orange", "apple", "orange", "banana", "kiwi", "banana"]

    # Count frequencies of each fruit
    fruit_counts = count_frequencies(fruits)

    # Print the results
    print("Fruit Frequencies:", fruit_counts)

    # Most common fruits
    most_common = fruit_counts.most_common(2)
    print("Most Common Fruits:", most_common)

if __name__ == "__main__":
    main()