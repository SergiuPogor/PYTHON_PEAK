from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = field(default=0)

    def total_price(self) -> float:
        return self.price * self.quantity

def main():
    # Create product instances
    product1 = Product(name="Laptop", price=999.99, quantity=3)
    product2 = Product(name="Mouse", price=19.99)

    # Display total price for each product
    print(f"Total price for {product1.name}: ${product1.total_price():.2f}")
    print(f"Total price for {product2.name}: ${product2.total_price():.2f}")

if __name__ == "__main__":
    main()