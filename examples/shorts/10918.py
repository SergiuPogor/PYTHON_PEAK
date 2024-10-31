# Efficiently Sorting a List of Dictionaries by a Specific Key
# Let's say we have a list of dictionaries representing orders in an e-commerce app

orders = [
    {"order_id": 102, "total": 235.50, "status": "shipped"},
    {"order_id": 67, "total": 112.90, "status": "pending"},
    {"order_id": 290, "total": 89.00, "status": "canceled"},
    {"order_id": 17, "total": 410.75, "status": "shipped"},
    {"order_id": 215, "total": 225.00, "status": "delivered"}
]

# Sort by 'total' in ascending order
sorted_by_total = sorted(orders, key=lambda x: x.get('total', 0))

# Sort by 'status' in alphabetical order, handling potential missing values by defaulting to empty string
sorted_by_status = sorted(orders, key=lambda x: x.get('status', ''))

# Sort by 'order_id' in descending order
sorted_by_order_id_desc = sorted(orders, key=lambda x: x.get('order_id', 0), reverse=True)

# Output each sorted list for visual comparison
print("Sorted by Total (asc):", sorted_by_total)
print("Sorted by Status (asc):", sorted_by_status)
print("Sorted by Order ID (desc):", sorted_by_order_id_desc)