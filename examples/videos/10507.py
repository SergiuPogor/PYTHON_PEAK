import pandas as pd

# Sample data mimicking a real-world use case, such as sales data
data = {
    'Product': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D'],
    'Region': ['North', 'South', 'West', 'North', 'South', 'North', 'West', 'South', 'North', 'West'],
    'Sales': [250, 150, 300, 400, 200, 100, 350, 120, 450, 500],
    'Discount': [10, 15, 5, 20, 0, 5, 10, 15, 10, 20]
}

df = pd.DataFrame(data)

# Using groupby and agg() for multi-level aggregation:
# Aggregating total sales and average discount per product
agg_df = df.groupby('Product').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Discount=('Discount', 'mean')
)

print("Aggregated DataFrame (Total Sales & Average Discount):")
print(agg_df)

# Now let's add more complexity by applying different aggregation functions
# per column and multiple functions per column
complex_agg_df = df.groupby('Product').agg(
    Total_Sales=('Sales', 'sum'),
    Sales_Stats=('Sales', ['mean', 'max', 'min']),
    Avg_Discount=('Discount', 'mean')
)

print("\nAggregated DataFrame with Complex Aggregation:")
print(complex_agg_df)

# Real-world scenario: conditional aggregation
# Let's add a condition: sum of sales where discount is greater than 10
conditional_agg_df = df[df['Discount'] > 10].groupby('Product').agg(
    Conditional_Sales=('Sales', 'sum'),
    Conditional_Avg_Discount=('Discount', 'mean')
)

print("\nAggregated DataFrame with Conditional Aggregation (Discount > 10):")
print(conditional_agg_df)

# Example showing how to apply custom lambda functions
custom_agg_df = df.groupby('Product').agg(
    Total_Sales=('Sales', 'sum'),
    Max_Discount=('Discount', lambda x: x.max() - x.min()),  # Custom range of discount
    Discount_Median=('Discount', 'median')
)

print("\nAggregated DataFrame with Custom Lambda Functions:")
print(custom_agg_df)

# In case you need to filter the results further or chain operations
filtered_agg_df = (
    df.groupby('Region')
    .agg(Total_Sales=('Sales', 'sum'), Avg_Discount=('Discount', 'mean'))
    .query('Total_Sales > 300')  # Filtering only regions with sales over 300
)

print("\nAggregated and Filtered DataFrame (Regions with Total Sales > 300):")
print(filtered_agg_df)

# Writing to a file, like '/tmp/test/input.txt', after processing
filtered_agg_df.to_csv('/tmp/test/aggregated_sales.txt', index=False)