def display_data(name, value, width=20, precision=2):
    # Format and print the data with specific width and precision
    formatted_string = f"{name:<{width}}: {value:.{precision}f}"
    print(formatted_string)

def main():
    # Example usage of display_data function
    data_entries = [
        ("Temperature", 23.456),
        ("Humidity", 56.789),
        ("Pressure", 1013.25)
    ]

    for entry in data_entries:
        display_data(entry[0], entry[1])

if __name__ == "__main__":
    main()
