from itertools import zip_longest

# Sample lists with different lengths
names = ["Alice", "Bob", "Charlie", "David"]
ages = [24, 30, 22]

# Using zip_longest to pair elements
def pair_lists(names, ages):
    paired = zip_longest(names, ages, fillvalue="N/A")
    return list(paired)

if __name__ == "__main__":
    result = pair_lists(names, ages)
    
    # Displaying the paired results
    for name, age in result:
        print(f"Name: {name}, Age: {age}")