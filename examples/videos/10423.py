from functools import partial
from typing import List

# Original function to calculate final price with tax and discount
def calculate_price(base_price: float, tax_rate: float, discount: float) -> float:
    # Calculate the total after tax and apply discount
    total = base_price * (1 + tax_rate) * (1 - discount)
    return round(total, 2)

# Use functools.partial to create pre-configured versions of the function for different tax scenarios
calculate_with_tax_10 = partial(calculate_price, tax_rate=0.10)
calculate_with_tax_20 = partial(calculate_price, tax_rate=0.20)

# Apply 10% tax and different discounts
price_10_no_discount = calculate_with_tax_10(base_price=100.00, discount=0.0)
price_10_with_discount = calculate_with_tax_10(base_price=100.00, discount=0.15)

# Apply 20% tax and different discounts
price_20_no_discount = calculate_with_tax_20(base_price=100.00, discount=0.0)
price_20_with_discount = calculate_with_tax_20(base_price=100.00, discount=0.15)

# Display all prices calculated using partial functions
print(f"Price with 10% tax, no discount: ${price_10_no_discount}")
print(f"Price with 10% tax, 15% discount: ${price_10_with_discount}")
print(f"Price with 20% tax, no discount: ${price_20_no_discount}")
print(f"Price with 20% tax, 15% discount: ${price_20_with_discount}")

# Advanced example: Partial function for file processing with dynamic file paths
def process_file(file_path: str, encoding: str, read_size: int) -> List[str]:
    # Reads file in chunks for memory efficiency
    lines = []
    with open(file_path, 'r', encoding=encoding) as file:
        while chunk := file.read(read_size):
            lines.extend(chunk.splitlines())
    return lines

# Partial function for processing large files with fixed parameters
process_large_file = partial(process_file, encoding='utf-8', read_size=1024)

# Process a specific file with predefined encoding and read size
file_data = process_large_file(file_path='/tmp/test/input.txt')

# Print lines read from file
print(f"Lines read from file: {len(file_data)}")
for line in file_data[:5]:  # Display only first 5 lines for brevity
    print(line)