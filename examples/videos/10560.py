import pdb

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    
    # Debugging point: Check if count is zero to avoid division by zero
    pdb.set_trace()  # Set a breakpoint here
    average = total / count if count > 0 else 0
    return average

def main():
    data = [10, 20, 30, 40, 50]
    average = calculate_average(data)
    print(f"The average is: {average}")

if __name__ == "__main__":
    main()

# Example of debugging a function that might throw an error
def process_data(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    processed_data = [int(line.strip()) for line in content]
    
    # Set a breakpoint to inspect the processed data
    pdb.set_trace()  # Debugging here to check the processed data
    return calculate_average(processed_data)

# Running the process_data function with a sample file
if __name__ == "__main__":
    result = process_data('/tmp/test/input.txt')
    print(f"Processed average: {result}")