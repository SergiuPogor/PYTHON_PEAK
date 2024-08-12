# example_value_error.py

class TemperatureConverter:
    def __init__(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be a number.")
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

def main():
    try:
        # Simulate user input
        temp_input = -300  # Example of an invalid input that should raise a ValueError
        converter = TemperatureConverter(temp_input)
        fahrenheit = converter.to_fahrenheit()
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    except ValueError as ve:
        print(f"ValueError encountered: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()











