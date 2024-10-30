from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)

@dataclass
class ShoppingCart:
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)

    def total_price(self) -> float:
        return sum(product.price for product in self.products)

    def list_products(self):
        for product in self.products:
            print(f"Product: {product.name}, Price: {product.price}, Tags: {product.tags}")

if __name__ == "__main__":
    # Create products
    apple = Product(name="Apple", price=0.5, tags=["fruit", "fresh"])
    banana = Product(name="Banana", price=0.3, tags=["fruit", "fresh"])
    broccoli = Product(name="Broccoli", price=1.2, tags=["vegetable", "healthy"])

    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(apple)
    cart.add_product(banana)
    cart.add_product(broccoli)

    # List products and total price
    cart.list_products()
    print("Total Price:", cart.total_price())