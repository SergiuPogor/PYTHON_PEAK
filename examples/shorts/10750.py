import pandas as pd

# Sample dataset creation
data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, None, 30, 22],
    "Salary": [70000, 80000, None, 50000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Data cleaning: Filling missing values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Display cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# Analysis: Basic statistics
statistics = df.describe()
print("\nBasic Statistics:")
print(statistics)