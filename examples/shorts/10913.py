# Pandas Data Analysis - Real-life Example

import pandas as pd
import numpy as np

# Sample Data: Employee performance with missing values and categorical data
data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Department": ["Sales", "Marketing", "Sales", "Engineering", np.nan],
    "ProjectsCompleted": [5, np.nan, 9, 3, 2],
    "MonthlyHours": [160, 150, np.nan, 200, 180],
    "SatisfactionScore": [4.3, 4.0, 3.8, np.nan, 4.5]
}

df = pd.DataFrame(data)

# Step 1: Fill missing values with column means where appropriate
df["ProjectsCompleted"].fillna(df["ProjectsCompleted"].mean(), inplace=True)
df["MonthlyHours"].fillna(df["MonthlyHours"].mean(), inplace=True)
df["SatisfactionScore"].fillna(df["SatisfactionScore"].mean(), inplace=True)

# Step 2: Group by 'Department' and calculate summary stats
summary = df.groupby("Department").agg({
    "ProjectsCompleted": "sum",
    "MonthlyHours": "mean",
    "SatisfactionScore": "mean"
}).rename(columns={
    "ProjectsCompleted": "TotalProjects",
    "MonthlyHours": "AvgMonthlyHours",
    "SatisfactionScore": "AvgSatisfaction"
})

# Step 3: Add a column to calculate each employee’s efficiency
df["EfficiencyScore"] = df["ProjectsCompleted"] / df["MonthlyHours"]

# Output final DataFrames
print("Cleaned Data:")
print(df)
print("\nDepartment Summary:")
print(summary)