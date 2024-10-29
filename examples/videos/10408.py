from pydantic import BaseModel, ValidationError, constr

class User(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: str
    age: int

def validate_user_input(data):
    try:
        user = User(**data)
        print("User input is valid:", user)
    except ValidationError as e:
        print("Validation errors:", e.errors())

def main():
    # Valid user input
    valid_input = {
        "username": "user123",
        "email": "user@example.com",
        "age": 25
    }
    validate_user_input(valid_input)

    # Invalid user input (age is negative)
    invalid_input = {
        "username": "us",
        "email": "user@example",
        "age": -5
    }
    validate_user_input(invalid_input)

    # Invalid user input (username too short)
    invalid_input_2 = {
        "username": "us",
        "email": "user@example.com",
        "age": 30
    }
    validate_user_input(invalid_input_2)

if __name__ == "__main__":
    main()