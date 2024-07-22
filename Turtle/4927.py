import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")

# Create a turtle object
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.width(2)

# Generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw a colorful spiral pattern
def draw_spiral():
    for i in range(300):
        color = random_color()
        screen.colormode(255)  # Set color mode to 255 for RGB
        spiral_turtle.pencolor(color)
        spiral_turtle.forward(i * 2)
        spiral_turtle.right(45)

# Center the spiral on the screen
spiral_turtle.penup()
spiral_turtle.goto(0, 0)
spiral_turtle.pendown()

# Draw the spiral
draw_spiral()

# Hide the turtle
spiral_turtle.hideturtle()

# Keep the window open
turtle.done()