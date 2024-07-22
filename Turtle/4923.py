import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)  # Set to full screen
screen.bgcolor("black")

# Create turtle object
vibrations = turtle.Turtle()
vibrations.speed(0)  # Set to the fastest speed

# Function to generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# Set color mode to 255 for RGB values
turtle.colormode(255)

# Function to calculate the width and height of the drawing
def calculate_dimensions(length, angle, step, repeat):
    total_length = length + step * (repeat - 1)
    width = total_length * 2 * (1 + abs(math.cos(math.radians(angle))))
    height = total_length * (1 + abs(math.sin(math.radians(angle))))
    return width, height

# Draw melodic vibrations function
def draw_vibrations(turtle_obj, length, angle, step, repeat):
    for _ in range(repeat):
        turtle_obj.color(random_color())
        turtle_obj.forward(length)
        turtle_obj.right(angle)
        turtle_obj.forward(length)
        turtle_obj.right(180 - angle)
        turtle_obj.forward(length)
        turtle_obj.right(angle)
        turtle_obj.forward(length)
        turtle_obj.right(180 - angle)
        length += step

# Initial parameters
initial_length = 10
angle = 60
step = 2  # Reduce step to avoid going off-screen quickly
repeat = 200  # Increase the repeat count

# Calculate dimensions
width, height = calculate_dimensions(initial_length, angle, step, repeat)

# Ensure the drawing stays within the screen
max_width, max_height = screen.window_width(), screen.window_height()
if width > max_width or height > max_height:
    scale_factor = min(max_width / width, max_height / height)
    initial_length *= scale_factor
    step *= scale_factor
    width, height = calculate_dimensions(initial_length, angle, step, repeat)

# Move the turtle to the starting position
start_x = -width // 2
start_y = height // 2
vibrations.penup()
vibrations.goto(start_x, start_y)
vibrations.pendown()

# Draw the melodic vibrations
draw_vibrations(vibrations, initial_length, angle, step, repeat)

# Hide the turtle and display the result
vibrations.hideturtle()
turtle.done()

