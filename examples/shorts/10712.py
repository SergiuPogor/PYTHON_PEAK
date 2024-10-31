from dataclasses import dataclass, replace
from datetime import datetime

# Define a class to represent an Order with various details
@dataclass
class Order:
    order_id: int
    customer: str
    status: str
    created_at: datetime
    total_amount: float

# Initial instance with original details
order = Order(
    order_id=101,
    customer="Alice",
    status="Pending",
    created_at=datetime.now(),
    total_amount=199.99
)

# Use dataclasses.replace() to create a modified copy without changing the original
updated_order = replace(order, status="Shipped", total_amount=209.99)

# Show results
print("Original Order:", order)
print("Updated Order:", updated_order)

# Imagine a bulk order scenario, updating orders with `dataclasses.replace`
bulk_orders = [
    Order(order_id=102, customer="Bob", status="Pending", created_at=datetime.now(), total_amount=89.50),
    Order(order_id=103, customer="Charlie", status="Pending", created_at=datetime.now(), total_amount=120.00),
]

# Update each order to 'Processed' and adjust total by a discount
processed_orders = [
    replace(order, status="Processed", total_amount=order.total_amount * 0.9)
    for order in bulk_orders
]

print("\nProcessed Orders with Discount:")
for o in processed_orders:
    print(o)