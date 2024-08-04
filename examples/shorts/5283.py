# Practical use of float() in a real-world scenario

# Example: Converting string inputs to float for mathematical operations

prices = ["10.99", "23.45", "4.50", "19.99"]
float_prices = list(map(float, prices))
total_price = sum(float_prices)
print(f"Total price: {total_price}")

# Example: Handling numerical precision in user inputs

user_inputs = ["0.1", "0.2", "0.3"]
float_inputs = list(map(float, user_inputs))
precision_check = sum(float_inputs)
print(f"Sum with precision check: {precision_check}")

# Example: Converting mixed-type list to float

mixed_values = [1, "2.5", "3", 4.75, "5.0"]
float_values = list(map(float, mixed_values))
average_value = sum(float_values) / len(float_values)
print(f"Average value: {average_value}")

# Example: Reading and converting data from a file

file_path = '/tmp/test/input.txt'

try:
    with open(file_path, 'r') as file:
        data = file.readlines()
        float_data = list(map(float, data))
        max_value = max(float_data)
        print(f"Maximum value in file: {max_value}")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except ValueError:
    print("File contains non-numeric values.")