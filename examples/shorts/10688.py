import pandas as pd

# Sample data for demonstration
data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'C', 'A'],
    'Value': [10, 20, 30, 40, 50, 60, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum and average
result = df.groupby('Category').agg(
    Total_Value=('Value', 'sum'),
    Average_Value=('Value', 'mean')
).reset_index()

# Print the result
print(result)