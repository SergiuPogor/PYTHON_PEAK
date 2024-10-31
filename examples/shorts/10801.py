# Code Example: Using dataclasses.asdict for Efficient Object Serialization

from dataclasses import dataclass, asdict, field
from typing import List, Optional

# Define nested dataclasses to represent a more complex data structure
@dataclass
class Address:
    street: str
    city: str
    zipcode: str

@dataclass
class User:
    name: str
    age: Optional[int]  # Handles None gracefully
    addresses: List[Address] = field(default_factory=list)

# Sample data to serialize
user_data = User(
    name="Alice Smith",
    age=None,  # None value included to test serialization handling
    addresses=[
        Address(street="123 Maple Street", city="Springfield", zipcode="12345"),
        Address(street="456 Oak Avenue", city="Shelbyville", zipcode="67890")
    ]
)

# Serialize User object to a dictionary
user_dict = asdict(user_data)

# Display serialized dictionary to verify structure and None handling
print("Serialized User Data:", user_dict)

# Sample output:
# {
#     'name': 'Alice Smith',
#     'age': None,
#     'addresses': [
#         {'street': '123 Maple Street', 'city': 'Springfield', 'zipcode': '12345'},
#         {'street': '456 Oak Avenue', 'city': 'Shelbyville', 'zipcode': '67890'}
#     ]
# }