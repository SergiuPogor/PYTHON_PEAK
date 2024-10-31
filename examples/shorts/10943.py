# Example of using the format() method for cleaner strings

def format_user_info(name, age, city):
    return "My name is {}, I am {} years old, and I live in {}.".format(name, age, city)

# Using named placeholders for clearer syntax
def format_item_info(item, price, quantity):
    return "Item: {item_name}, Price: ${price:.2f}, Quantity: {qty}".format(
        item_name=item,
        price=price,
        qty=quantity
    )

# Usage examples
user_info = format_user_info("Alice", 30, "New York")
item_info = format_item_info("Apple", 0.5, 10)

print(user_info)  # Output: My name is Alice, I am 30 years old, and I live in New York.
print(item_info)  # Output: Item: Apple, Price: $0.50, Quantity: 10