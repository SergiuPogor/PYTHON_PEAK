class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"

# List of product objects
products = [
    Product("Laptop", 1200),
    Product("Smartphone", 800),
    Product("Headphones", 150)
]

# Find the product with the lowest price
cheapest_product = min(products, key=lambda p: p.price)
print("Cheapest product:", cheapest_product)