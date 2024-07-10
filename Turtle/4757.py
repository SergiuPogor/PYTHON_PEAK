import random
import turtle


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Stunning Geometric Patterns with Python Turtle")

# Create a turtle named "artist"
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed
artist.width(2)

# Define colors
colors = ["red", "yellow", "blue", "green", "purple", "orange"]


# Function to draw a geometric pattern
def draw_geometric_pattern(radius, num_circles, num_patterns):
    for i in range(num_patterns):
        artist.color(random.choice(colors))
        for j in range(num_circles):
            angle = 360 / num_circles
            artist.circle(radius)
            artist.right(angle)
        artist.right(360 / num_patterns)


# Draw multiple geometric patterns
for _ in range(10):  # Feel free to increase/decrease the number of patterns
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    radius = random.randint(50, 150)
    num_circles = random.randint(6, 12)
    num_patterns = random.randint(4, 8)
    draw_geometric_pattern(radius, num_circles, num_patterns)

# Hide the turtle and display the result
artist.hideturtle()
turtle.done()

