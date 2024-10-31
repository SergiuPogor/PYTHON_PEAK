# Code Example: Using property Decorators for Attribute Validation and Control

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Property for name with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    # Property for price with read-only access and rounding
    @property
    def price(self):
        return round(self._price, 2)

    # Property to calculate discounted price on-the-fly
    @property
    def discounted_price(self):
        return round(self._price * 0.9, 2)

# Example Usage
try:
    p = Product("Laptop", 1499.99)
    print(f"Name: {p.name}")                # "Laptop"
    print(f"Price: ${p.price}")             # "$1499.99"
    print(f"Discounted Price: ${p.discounted_price}")  # "$1349.99"
    
    p.name = "Tablet"                       # Valid update
    print(f"Updated Name: {p.name}")        # "Tablet"
    
    p.name = " "                            # Triggers ValueError: "Name cannot be empty."
except ValueError as e:
    print(e)