class CustomList(list):
    def max_value(self):
        """Return the maximum value from the list."""
        if not self:
            raise ValueError("List is empty")
        return max(self)

    def min_value(self):
        """Return the minimum value from the list."""
        if not self:
            raise ValueError("List is empty")
        return min(self)

    def average(self):
        """Return the average of the list values."""
        if not self:
            raise ValueError("List is empty")
        return sum(self) / len(self)

    def __str__(self):
        """Return a string representation of the CustomList."""
        return f"CustomList({super().__str__()})"

# Example usage
if __name__ == "__main__":
    # Create an instance of CustomList
    my_list = CustomList([10, 20, 30, 40, 50])
    
    # Display the list
    print("My Custom List:", my_list)
    
    # Get maximum value
    print("Max Value:", my_list.max_value())
    
    # Get minimum value
    print("Min Value:", my_list.min_value())
    
    # Get average value
    print("Average:", my_list.average())
    
    # Adding more values
    my_list.append(60)
    print("Updated Custom List:", my_list)
    
    # Get maximum value again
    print("New Max Value:", my_list.max_value())