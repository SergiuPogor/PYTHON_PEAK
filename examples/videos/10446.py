import pandas as pd

def data_manipulation_example():
    """
    Demonstrate powerful data manipulation with Pandas.
    This example shows data cleaning, filtering, and aggregation.
    """
    # Sample data: a dictionary representing a dataset
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
        'Age': [24, 30, 22, 35, 29],
        'Salary': [50000, 54000, 58000, 62000, 61000],
        'Department': ['HR', 'Finance', 'IT', 'IT', 'HR']
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Clean data: Filter out employees younger than 25
    df_filtered = df[df['Age'] >= 25]

    # Display filtered DataFrame
    print("\nFiltered DataFrame (Age >= 25):")
    print(df_filtered)

    # Group by Department and calculate average salary
    avg_salary = df.groupby('Department')['Salary'].mean().reset_index()

    # Display average salary by department
    print("\nAverage Salary by Department:")
    print(avg_salary)

    # Sort employees by Salary in descending order
    df_sorted = df.sort_values(by='Salary', ascending=False)

    # Display sorted DataFrame
    print("\nSorted DataFrame by Salary (Descending):")
    print(df_sorted)

# Run the data manipulation example
data_manipulation_example()