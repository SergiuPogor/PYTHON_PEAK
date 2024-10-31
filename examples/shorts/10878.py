from pydantic import BaseModel, Field, ValidationError, HttpUrl
from typing import List, Optional

# Define a data model with validation rules
class UserModel(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=30)
    email: str
    age: Optional[int] = Field(default=None, gt=13)  # Age must be >13 if provided
    website: Optional[HttpUrl]  # Checks if website is a valid URL
    skills: List[str] = Field(min_items=1)  # Must have at least one skill

# Create a test data function to demonstrate validation
def validate_user_data(data):
    try:
        user = UserModel(**data)
        print("Validated User Data:", user)
    except ValidationError as e:
        print("Validation Errors:", e.json())

# Test cases: one valid and one invalid
test_data_valid = {
    "id": 101,
    "username": "techguru",
    "email": "guru@example.com",
    "age": 29,
    "website": "https://example.com",
    "skills": ["Python", "Data Science"]
}

test_data_invalid = {
    "id": "XYZ",  # Invalid type
    "username": "tg",  # Too short
    "email": "guru@example.com",
    "age": 10,  # Too young
    "website": "not-a-valid-url",  # Invalid URL
    "skills": []  # Missing skills
}

validate_user_data(test_data_valid)    # Expected: Validation success
validate_user_data(test_data_invalid)  # Expected: Validation errors