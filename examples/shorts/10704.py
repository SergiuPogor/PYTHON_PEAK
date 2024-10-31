from collections import namedtuple

# Define a namedtuple for a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

def create_point(x, y):
    # Create a point instance
    return Point(x, y)

def main():
    point1 = create_point(10, 20)
    point2 = create_point(30, 40)

    print(f"Point 1: x = {point1.x}, y = {point1.y}")
    print(f"Point 2: x = {point2.x}, y = {point2.y}")

    # Accessing elements by name improves readability
    distance = ((point2.x - point1.x) ** 2 + 
                (point2.y - point1.y) ** 2) ** 0.5
    print(f"Distance between points: {distance:.2f}")

if __name__ == "__main__":
    main()