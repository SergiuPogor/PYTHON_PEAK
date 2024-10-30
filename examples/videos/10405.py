# Using setdefault to simplify dictionary initialization

def group_animals(animals):
    grouped = {}
    for animal in animals:
        # Use setdefault to initialize a list if the key doesn't exist
        grouped.setdefault(animal['type'], []).append(animal['name'])
    return grouped

def main():
    animals = [
        {'name': 'Dog', 'type': 'Mammal'},
        {'name': 'Cat', 'type': 'Mammal'},
        {'name': 'Frog', 'type': 'Amphibian'},
        {'name': 'Goldfish', 'type': 'Fish'},
        {'name': 'Lizard', 'type': 'Reptile'},
        {'name': 'Sparrow', 'type': 'Bird'}
    ]

    grouped_animals = group_animals(animals)
    print("Grouped Animals:", grouped_animals)

if __name__ == "__main__":
    main()