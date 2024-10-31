from pydantic import BaseModel, EmailStr, ValidationError

# Define a data model using Pydantic
class User(BaseModel):
    name: str
    age: int
    email: EmailStr

def main():
    try:
        # Create a user instance with valid data
        user = User(name="Alice", age=30, email="alice@example.com")
        print(user)

        # Attempt to create a user with invalid email
        invalid_user = User(name="Bob", age=25, email="not-an-email")
    except ValidationError as e:
        # Catch validation errors and print them
        print("Validation errors:", e)

if __name__ == "__main__":
    main()