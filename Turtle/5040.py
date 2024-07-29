import turtle
import random

# Setup the screen with 1920x1080 resolution
screen = turtle.Screen()
screen.setup(width=1920, height=1080)

# Create a turtle named "designer" with a specific shape
designer = turtle.Turtle()
designer.speed(0)  # Maximum speed for quick drawing

# Move the turtle to the center for symmetry
designer.penup()
designer.goto(0, 0)
designer.pendown()

# Define a function to draw a colorful geometric pattern with multiple levels
def draw_geometric_pattern(t, size, repetitions, levels):
    angle = 360 / repetitions  # Divide 360 degrees by the number of repetitions
    for level in range(levels):
        for _ in range(repetitions):
            # Set random RGB colors
            t.color(random.random(), random.random(), random.random())
            for _ in range(4):  # Draw a square
                t.forward(size)
                t.right(90)
            t.right(angle)  # Rotate the turtle for the next repetition
        size /= 1.5  # Reduce the size for the next level
        t.penup()
        t.goto(0, 0)
        t.pendown()

# Call the function with specific parameters
draw_geometric_pattern(designer, 300, 36, 5)

# Hide the turtle after drawing
designer.hideturtle()

# Keep the window open until clicked
screen.exitonclick()

