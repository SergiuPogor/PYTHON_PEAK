from collections import defaultdict

def group_items(data):
    # Create a defaultdict with list as default factory
    grouped = defaultdict(list)

    # Group data by category
    for item in data:
        category = item['category']
        grouped[category].append(item['name'])

    return dict(grouped)

if __name__ == "__main__":
    # Example data: a list of items with categories
    items = [
        {'name': 'Apple', 'category': 'Fruit'},
        {'name': 'Banana', 'category': 'Fruit'},
        {'name': 'Broccoli', 'category': 'Vegetable'},
        {'name': 'Carrot', 'category': 'Vegetable'},
        {'name': 'Chicken', 'category': 'Meat'},
        {'name': 'Beef', 'category': 'Meat'},
    ]

    # Group the items
    result = group_items(items)

    # Print the grouped result
    print("Grouped items:", result)