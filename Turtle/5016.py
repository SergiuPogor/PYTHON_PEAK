import math
import turtle

# Setup screen for 1920x1080 resolution
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Complex 3D Illusion")
screen.setup(width=1920, height=1080)

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Global variable to keep track of gradient progress
gradient_step = 0
gradient_max_steps = 360  # Number of steps in the gradient (full color cycle)


# Function to convert RGB values to turtle's color format (0-1 range)
def rgb_to_turtle_color(r, g, b):
    return (r / 255.0, g / 255.0, b / 255.0)


# Function to get the next gradient color
def get_next_gradient_color():
    global gradient_step
    # Calculate the RGB values for the current step
    r = (gradient_step % 256)  # Red component varies from 0 to 255
    g = ((gradient_step + 85) % 256)  # Green component varies from 85 to 255
    b = ((gradient_step + 170) % 256)  # Blue component varies from 170 to 255

    # Convert RGB to turtle color format
    color = rgb_to_turtle_color(r, g, b)

    gradient_step = (gradient_step + 1) % (256 * 3)  # Increment and wrap around
    return color


# Function to draw a 3D illusion pattern
def draw_pattern(t, radius, angle, depth, factor):
    for i in range(depth):
        angle_rad = math.radians(angle + i * factor)
        x = radius * math.cos(angle_rad)
        y = radius * math.sin(angle_rad) + 100

        # Update color for each segment
        color = get_next_gradient_color()

        t.color(color)

        t.penup()
        t.goto(x, y)
        t.pendown()

        for j in range(6):
            t.forward(radius / 2)
            t.right(60)


# Animation loop
iterations = 2000  # Number of patterns to draw
angle_increment = 2
radius = 300
depth = 72
factor = 5

for step in range(1, iterations + 1):
    # Draw pattern for current step
    draw_pattern(t, radius, step * angle_increment, depth, factor)

# Keeps the window open
turtle.done()

