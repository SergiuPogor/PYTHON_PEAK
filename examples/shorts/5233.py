# Example: Using abs() function for practical mathematical operations

# Scenario: Calculating the distance between two points in a 2D space
point_a = (3, -4)
point_b = (-1, 2)

# Calculate the distance using the abs() function
distance = abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
print(distance)  # Output: 10

# Another example: Ensuring positive transaction values in a financial application
transactions = [-100, 200, -50, 400, -75]
positive_transactions = [abs(amount) for amount in transactions]
print(positive_transactions)  # Output: [100, 200, 50, 400, 75]

# Example: Avoiding negative results in a custom scoring system
def calculate_score(points):
    # Ensure the score is always positive
    return abs(points)

scores = [-10, 15, -8, 20, -5]
adjusted_scores = [calculate_score(score) for score in scores]
print(adjusted_scores)  # Output: [10, 15, 8, 20, 5]

# Another scenario: Normalizing sensor data
sensor_readings = [-0.5, 0.3, -0.2, 0.8, -0.1]
normalized_readings = [abs(reading) for reading in sensor_readings]
print(normalized_readings)  # Output: [0.5, 0.3, 0.2, 0.8, 0.1]