import pandas as pd

# Sample data creation
data = {
    'Category': ['Fruit', 'Fruit', 'Vegetable', 'Vegetable', 'Fruit'],
    'Item': ['Apple', 'Banana', 'Carrot', 'Broccoli', 'Orange'],
    'Price': [1.5, 0.75, 1.0, 1.25, 1.3],
    'Quantity': [10, 20, 15, 10, 5]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Grouping by 'Category' and calculating total price and average price
grouped = df.groupby('Category').agg(
    Total_Price=('Price', 'sum'),
    Average_Price=('Price', 'mean')
).reset_index()

# Display the grouped data
print(grouped)