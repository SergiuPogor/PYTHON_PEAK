import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")

# Create the turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest speed
spiral.width(2)

# Function to generate random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw the hypnotic spiral
for i in range(360):
    spiral.color(random_color())
    spiral.forward(i * 2)
    spiral.right(59)
    spiral.penup()
    spiral.goto(0, 0)  # Center the spiral
    spiral.pendown()

# Hide the turtle and display the result
spiral.hideturtle()
turtle.done()