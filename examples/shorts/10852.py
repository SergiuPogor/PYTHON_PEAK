import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'Score': [85, 90, 95, 80, 70, 90],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science']
}

# Create DataFrame
df = pd.DataFrame(data)

# Grouping by Name and Subject and calculating average Score
grouped = df.groupby(['Name', 'Subject']).agg(
    Average_Score=('Score', 'mean'),
    Total_Scores=('Score', 'sum')
).reset_index()

# Displaying the grouped DataFrame
print(grouped)