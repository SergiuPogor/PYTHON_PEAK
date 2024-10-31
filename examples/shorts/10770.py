def process_data(data):
    try:
        # Simulating possible errors
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        if len(data) == 0:
            raise IndexError("List cannot be empty")
        
        # Process data
        return [x * 2 for x in data]

    except (ValueError, IndexError) as e:
        print(f"Error occurred: {e}")
        return None

# Example data
data1 = [1, 2, 3]
data2 = "Not a list"
data3 = []

# Testing the function
print(process_data(data1))  # Should return [2, 4, 6]
print(process_data(data2))  # Should print an error message
print(process_data(data3))  # Should print an error message