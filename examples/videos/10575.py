def calculate_area(radius):
    # Calculate the area of a circle
    return 3.14 * radius ** 2

def describe_circle(radius):
    area = calculate_area(radius)
    # Using f-strings for dynamic string formatting
    return f"A circle with a radius of {radius} has an area of {area:.2f}."

def main():
    # Sample radii for demonstration
    radii = [1, 2, 3.5, 4.2, 5]
    descriptions = []

    for r in radii:
        descriptions.append(describe_circle(r))

    # Print each description
    for desc in descriptions:
        print(desc)

if __name__ == "__main__":
    main()

# This code demonstrates the use of f-strings for
# formatting dynamic strings in Python. Each circle's
# description is generated using f-strings for clear
# and concise output, showcasing both radius and area.