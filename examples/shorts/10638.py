# Example: Using setdefault() to initialize dictionary keys for efficient data processing

data_log = [
    {"category": "error", "message": "File not found"},
    {"category": "warning", "message": "Memory usage high"},
    {"category": "info", "message": "Process started"},
    {"category": "error", "message": "Access denied"},
    {"category": "info", "message": "Process completed"}
]

# Categorize log entries without redundant key checks using setdefault
category_counts = {}
for log in data_log:
    category_counts.setdefault(log["category"], 0)
    category_counts[log["category"]] += 1

print("Log Counts by Category:", category_counts)

# Another use case: Collecting items by category
inventory = [
    {"category": "electronics", "item": "laptop"},
    {"category": "furniture", "item": "chair"},
    {"category": "electronics", "item": "mouse"},
    {"category": "furniture", "item": "table"},
    {"category": "electronics", "item": "keyboard"}
]

# Initialize and group items by category without checking each key
grouped_items = {}
for item in inventory:
    grouped_items.setdefault(item["category"], []).append(item["item"])

print("Items Grouped by Category:", grouped_items)

# setdefault is especially useful for efficient counting, categorizing, or grouping without repetitive key checks