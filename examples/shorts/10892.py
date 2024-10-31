import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Method 1: Fill missing values with the mean
df['A'].fillna(df['A'].mean(), inplace=True)

# Method 2: Drop rows with any missing values
df_dropped = df.dropna()

# Method 3: Interpolate to fill missing values
df['B'] = df['B'].interpolate()

# Display the results
print("\nDataFrame after filling missing values:")
print(df)
print("\nDataFrame after dropping missing values:")
print(df_dropped)