def get_validated_input(prompt, conversion_func, validation_func):
    while True:
        user_input = input(prompt)
        try:
            # Convert input to the desired type
            converted_input = conversion_func(user_input)
            # Validate the converted input
            if validation_func(converted_input):
                return converted_input
            else:
                print("Input is not valid. Please try again.")
        except ValueError:
            print("Invalid input type. Please enter a valid value.")

# Example usage
# Prompt user for an integer between 1 and 10
user_number = get_validated_input(
    "Enter a number between 1 and 10: ",
    int,
    lambda x: 1 <= x <= 10
)

print(f"You entered a valid number: {user_number}")
