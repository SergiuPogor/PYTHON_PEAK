from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

# Define a clean data structure for an e-commerce order
@dataclass
class Customer:
    id: int
    name: str
    email: str = field(repr=False)  # Hide sensitive info in repr

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Order:
    order_id: int
    customer: Customer
    items: List[Product]
    date_created: date = field(default_factory=date.today)  # Automatic default for today's date
    shipped: bool = False  # A default field

    def total_cost(self) -> float:
        return sum(item.price for item in self.items)

# Example usage
customer1 = Customer(id=101, name="Jane Doe", email="jane.doe@example.com")
product1 = Product(id=1, name="Laptop", price=1200.00)
product2 = Product(id=2, name="Mouse", price=25.00)
order1 = Order(order_id=5001, customer=customer1, items=[product1, product2])

# Accessing order details and calculating total cost
print(f"Order for {order1.customer.name}: ${order1.total_cost()}")

# Compare two instances to show how dataclasses handle equality by default
order2 = Order(order_id=5001, customer=customer1, items=[product1, product2])
print("Orders are identical:", order1 == order2)

# Updating the shipped status
order1.shipped = True
print(f"Order {order1.order_id} shipped status: {order1.shipped}")