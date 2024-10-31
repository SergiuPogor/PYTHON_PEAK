from collections import namedtuple

# Define a namedtuple for a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

def distance(point1, point2):
    # Calculate the distance between two points
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

def main():
    # Create two points using namedtuples
    point_a = Point(1, 2)
    point_b = Point(4, 6)

    # Calculate the distance between the two points
    dist = distance(point_a, point_b)
    print(f"The distance between {point_a} and {point_b} is {dist:.2f}")

if __name__ == "__main__":
    main()