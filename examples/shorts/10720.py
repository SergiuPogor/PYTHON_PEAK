import pandas as pd

# Path to large CSV file
file_path = '/tmp/test/large_data.csv'

# Define chunk size and process data in chunks to avoid memory overload
chunk_size = 10000  # Adjust size based on available memory and file size

# Initialize a DataFrame to store processed data
processed_data = pd.DataFrame()

# Iterate over chunks and perform data processing on each chunk
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Example of simple data processing: filtering data
    filtered_chunk = chunk[chunk['status'] == 'active']
    # Append processed chunk to the final DataFrame
    processed_data = pd.concat([processed_data, filtered_chunk])

# Perform additional actions on processed_data as needed
print("Processed data shape:", processed_data.shape)

# Save processed data to a new file, if required
processed_data.to_csv('/tmp/test/processed_data.csv', index=False)