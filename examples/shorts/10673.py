import pdb

# Sample function that calculates average but fails for empty list
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Empty list provided!")  # Guard clause for empty input
    return sum(numbers) / len(numbers)

# Enhanced debugging method using pdb for a complex workflow
def process_data(file_path):
    data = []
    with open(file_path) as file:
        for line in file:
            # Let's pause here to inspect each line read from file
            pdb.set_trace()
            data.append(int(line.strip()))
    avg = calculate_average(data)
    print("Average calculated:", avg)

# Trigger the function
try:
    process_data('/tmp/test/input.txt')
except Exception as e:
    print("Caught an exception:", e)

# Use pdb here to set a breakpoint before running main logic,
# letting us debug and inspect function flow and variable states.