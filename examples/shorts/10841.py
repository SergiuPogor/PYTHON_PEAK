from typing import Protocol, runtime_checkable

@runtime_checkable
class JSONSerializable(Protocol):
    def to_json(self) -> str:
        ...

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_json(self) -> str:
        return f'{{"name": "{self.name}", "age": {self.age}}}'

class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    # This class intentionally lacks a to_json method

def serialize_to_json(obj: JSONSerializable) -> str:
    return obj.to_json()

user = User("Alice", 30)
print(serialize_to_json(user))  # Works as User implements to_json

product = Product("Laptop", 1200.99)
# print(serialize_to_json(product))  # Uncommenting this line would raise an error