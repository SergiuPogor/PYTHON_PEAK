from collections import namedtuple
import time

# Define a NamedTuple for a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

def create_points(num_points):
    # Create a list of Point NamedTuples
    points = [Point(x, y) for x, y in zip(range(num_points), range(num_points))]
    return points

def calculate_distance(point1, point2):
    # Calculate the distance between two points
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

def main():
    num_points = 100000
    points = create_points(num_points)

    # Measure the time taken to calculate distances
    start_time = time.time()
    distances = [calculate_distance(points[i], points[i + 1]) for i in range(num_points - 1)]
    end_time = time.time()

    print(f"Calculated distances in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    main()