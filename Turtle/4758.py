import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mesmerizing Symmetric Patterns with Python Turtle")
screen.setup(width=1000, height=1000)

# Create turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed
artist.width(2)

# Define colors
colors = ["red", "yellow", "blue", "green", "purple", "orange"]


# Function to draw a single symmetric pattern
def draw_symmetric_pattern(radius, num_sides, num_patterns):
    angle = 360 / num_sides
    for i in range(num_patterns):
        artist.color(colors[i % len(colors)])  # Cycle through predefined colors
        for _ in range(num_sides):
            artist.forward(radius)
            artist.right(angle)
        artist.right(360 / num_patterns)


# Function to draw a complex pattern in the center
def draw_complex_pattern():
    center_x, center_y = 0, 0
    artist.penup()
    artist.goto(center_x, center_y)
    artist.pendown()
    layers = 8  # Number of layers in the complex pattern
    for layer in range(layers):
        radius = 100 + layer * 40  # Increase radius for each layer
        num_sides = 6  # Fixed number of sides for a consistent pattern
        num_patterns = 12  # Fixed number of patterns for a consistent pattern
        draw_symmetric_pattern(radius, num_sides, num_patterns)
        artist.right(360 / layers)  # Adjust rotation for symmetry


# Draw the complex pattern
draw_complex_pattern()

# Hide the turtle and display the result
artist.hideturtle()
turtle.done()

