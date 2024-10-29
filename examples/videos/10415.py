def calculate_stats(numbers):
    # This function returns mean, median, and mode of a list of numbers
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2 if len(numbers) % 2 == 0 else sorted_numbers[mid]
    
    # Calculate mode
    mode = max(set(numbers), key=numbers.count)
    
    return mean, median, mode  # Return multiple values as a tuple

# Usage example
if __name__ == '__main__':
    data = [1, 2, 2, 3, 4, 4, 4, 5, 6]
    
    # Using tuple unpacking to capture multiple return values
    avg, med, mod = calculate_stats(data)
    
    print("Statistics:")
    print(f"Mean: {avg:.2f}")  # Display mean
    print(f"Median: {med:.2f}")  # Display median
    print(f"Mode: {mod}")  # Display mode