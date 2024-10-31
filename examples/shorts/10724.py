from itertools import accumulate

# Sample data: monthly expenses
expenses = [200, 150, 300, 250, 100]

# Calculate running totals
running_totals = list(accumulate(expenses))

# Display results
for month, total in enumerate(running_totals, start=1):
    print(f"Total expenses after month {month}: ${total}")

# Example usage with a larger dataset
# Imagine these are daily sales
daily_sales = [120, 300, 200, 450, 600, 500, 700]
cumulative_sales = list(accumulate(daily_sales))

# Print cumulative sales
for day, total in enumerate(cumulative_sales, start=1):
    print(f"Total sales by day {day}: ${total}")