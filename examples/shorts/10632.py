# Use case: Aggregating monthly expenses for two different categories across months

months = ["January", "February", "March", "April"]
food_expenses = [200, 250, 210, 190]
entertainment_expenses = [100, 150, 120, 130]

# Using zip to iterate over months, food_expenses, and entertainment_expenses in parallel
print("Monthly Expenses (Food & Entertainment):")
for month, food, entertainment in zip(months, food_expenses, entertainment_expenses):
    total = food + entertainment
    print(f"{month}: Food = ${food}, Entertainment = ${entertainment}, Total = ${total}")

# Use case: Creating a dictionary from two lists, aligning months with total expenses
monthly_totals = dict(zip(months, [f + e for f, e in zip(food_expenses, entertainment_expenses)]))

print("\nMonthly Total Expenses:")
for month, total in monthly_totals.items():
    print(f"{month}: ${total}")