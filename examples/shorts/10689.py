class CustomList:
    def __init__(self, initial_data):
        self.data = initial_data

    def __getitem__(self, index):
        # Add custom behavior: Validate index
        if isinstance(index, int):
            if index < 0 or index >= len(self.data):
                raise IndexError("Index out of range")
            return self.data[index]
        else:
            raise TypeError("Invalid index type. Must be an integer.")

# Example usage
custom_list = CustomList([10, 20, 30, 40, 50])

# Accessing items using custom indexing
try:
    print(custom_list[2])  # Outputs: 30
    print(custom_list[5])  # Raises IndexError
except Exception as e:
    print(e)