# Code Example: Grouping Data by Multiple Keys with itertools.groupby

from itertools import groupby
from operator import itemgetter

# Sample dataset: list of transactions with category, date, and amount
transactions = [
    {"category": "food", "date": "2023-10-20", "amount": 20.5},
    {"category": "food", "date": "2023-10-21", "amount": 15.0},
    {"category": "transport", "date": "2023-10-20", "amount": 7.5},
    {"category": "food", "date": "2023-10-22", "amount": 12.3},
    {"category": "utilities", "date": "2023-10-20", "amount": 50.0},
    {"category": "transport", "date": "2023-10-21", "amount": 10.0},
    {"category": "utilities", "date": "2023-10-21", "amount": 40.0}
]

# Step 1: Sort the list by category and then by date for groupby to work correctly
transactions.sort(key=itemgetter("category", "date"))

# Step 2: Use itertools.groupby to group by category
for category, items in groupby(transactions, key=itemgetter("category")):
    print(f"\nCategory: {category}")
    for item in items:
        print(f"  Date: {item['date']}, Amount: ${item['amount']}")

# Step 3: Advanced Grouping by category, then further sub-group by date
print("\n--- Advanced Grouping ---")
for category, category_items in groupby(transactions, key=itemgetter("category")):
    print(f"\nCategory: {category}")
    for date, date_items in groupby(category_items, key=itemgetter("date")):
        amounts = [item["amount"] for item in date_items]
        print(f"  Date: {date}, Total Amount: ${sum(amounts)}")