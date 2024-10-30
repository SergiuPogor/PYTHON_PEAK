# Define a metaclass to enforce the presence of a specific method across subclasses
class MethodEnforcer(type):
    def __new__(cls, name, bases, dct):
        # Check if the class defines a 'validate' method, raise an error if not
        if 'validate' not in dct:
            raise TypeError(f"Class '{name}' must implement 'validate' method")
        return super().__new__(cls, name, bases, dct)

# Base class utilizing MethodEnforcer as its metaclass
class BaseEntity(metaclass=MethodEnforcer):
    def save(self):
        # Simulate saving data with validation
        if self.validate():
            print("Data saved successfully.")
        else:
            print("Data validation failed.")

# Subclass with the required 'validate' method
class Product(BaseEntity):
    def validate(self) -> bool:
        # Simple validation logic for Product class
        return hasattr(self, 'name') and hasattr(self, 'price')

# Subclass without the required 'validate' method, should raise an error
try:
    class Customer(BaseEntity):
        pass
except TypeError as e:
    print(e)

# Define another subclass with custom validation
class Order(BaseEntity):
    def validate(self) -> bool:
        # Example of specific validation for the Order class
        return hasattr(self, 'order_id') and isinstance(self.order_id, int)

# Use cases demonstrating enforcement
# Valid Product instance with validation check
product = Product()
product.name = "Laptop"
product.price = 1200.00
product.save()

# Invalid Product instance without setting required attributes
invalid_product = Product()
invalid_product.save()

# Valid Order instance with validation
order = Order()
order.order_id = 101
order.save()

# Invalid Order instance without 'order_id' attribute
invalid_order = Order()
invalid_order.save()