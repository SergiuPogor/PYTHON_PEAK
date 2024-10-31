import pandas as pd

def handle_missing_data(df):
    """Handle missing data in a DataFrame."""
    # Display initial data
    print("Initial DataFrame:")
    print(df)

    # Identify missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Fill missing values with the mean of each column
    df_filled = df.fillna(df.mean())
    
    # Display DataFrame after filling missing values
    print("\nDataFrame after filling missing values:")
    print(df_filled)

def main():
    # Create a sample DataFrame with missing values
    data = {
        'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, 2, 3, None]
    }
    df = pd.DataFrame(data)

    # Handle missing data
    handle_missing_data(df)

if __name__ == "__main__":
    main()