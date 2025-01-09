# Dictionary with multiple levels for tracking items by category and subcategory
store_inventory = {}

# Function to add items to nested dictionary with setdefault
def add_item(category: str, subcategory: str, item: str, quantity: int):
    # Initialize category and subcategory dictionaries if not already present
    if category not in store_inventory:
        store_inventory[category] = {}
    if subcategory not in store_inventory[category]:
        store_inventory[category][subcategory] = {}
    # Add or update the item quantity
    store_inventory[category][subcategory][item] = \
        store_inventory[category][subcategory].get(item, 0) + quantity

# Sample entries for store_inventory
add_item("Electronics", "Laptops", "Dell Inspiron", 5)
add_item("Electronics", "Laptops", "HP Pavilion", 3)
add_item("Electronics", "Phones", "iPhone 12", 10)
add_item("Clothing", "Men", "T-Shirt", 20)
add_item("Clothing", "Women", "Jacket", 15)
add_item("Clothing", "Kids", "Hat", 8)

# Printing the updated store inventory
print("Store Inventory:")
for category, subcategories in store_inventory.items():
    print(f"\nCategory: {category}")
    for subcategory, items in subcategories.items():
        print(f"  Subcategory: {subcategory}")
        for item, quantity in items.items():
            print(f"    {item}: {quantity}")

# Function to aggregate items across all categories
def get_total_items():
    total_items = {}
    for category, subcategories in store_inventory.items():
        for subcategory, items in subcategories.items():
            for item, quantity in items.items():
                total_items.setdefault(item, 0)
                total_items[item] += quantity
    return total_items

# Displaying aggregated items in store
print("\nTotal Items in Store:")
for item, quantity in get_total_items().items():
    print(f"  {item}: {quantity}")

# Special use case: Adding additional data sources
# Load pre-configured data and use setdefault for new data inputs
def update_inventory(data_source: dict):
    for category, subcategories in data_source.items():
        for subcategory, items in subcategories.items():
            for item, quantity in items.items():
                store_inventory.setdefault(category, {}).setdefault(subcategory, {}).setdefault(item, 0)
                store_inventory[category][subcategory][item] += quantity

# Test additional inventory update
new_data = {
    "Electronics": {
        "Tablets": {"Samsung Galaxy Tab": 7, "iPad": 3},
        "Phones": {"Google Pixel": 5, "iPhone 12": 4}
    },
    "Clothing": {
        "Women": {"Dress": 6, "Hat": 3},
        "Kids": {"Sweater": 10}
    }
}
update_inventory(new_data)

print("\nUpdated Store Inventory after merging new data:")
for category, subcategories in store_inventory.items():
    print(f"\nCategory: {category}")
    for subcategory, items in subcategories.items():
        print(f"  Subcategory: {subcategory}")
        for item, quantity in items.items():
            print(f"    {item}: {quantity}")

