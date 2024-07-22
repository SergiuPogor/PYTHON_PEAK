import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")

# Create a turtle object
meditation_turtle = turtle.Turtle()
meditation_turtle.speed(0)
meditation_turtle.width(2)


# Generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Draw a meditative consciousness layer pattern
def draw_layer(radius, angle_step):
    for _ in range(int(360 / angle_step)):
        color = random_color()
        screen.colormode(255)  # Set color mode to 255 for RGB
        meditation_turtle.pencolor(color)
        meditation_turtle.circle(radius)
        meditation_turtle.right(angle_step)


# Center the layers on the screen
def center_turtle(turtle, radius):
    turtle.penup()
    turtle.goto(0, -radius / 2)  # Center the turtle so the circle's center is on the screen
    turtle.pendown()


# Adjust radius and draw multiple layers to fit within 1920x1080
max_radius = 200  # Reduced the max radius to ensure it fits within the screen
layers = 5
base_radius = max_radius / layers

for i in range(layers):
    radius = base_radius + i * (max_radius / layers)
    center_turtle(meditation_turtle, radius)
    draw_layer(radius, 15)

# Hide the turtle
meditation_turtle.hideturtle()

# Keep the window open
turtle.done()

