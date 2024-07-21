import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Function to generate random color
def random_color():
    return random.random(), random.random(), random.random()

# Draw a symmetric X shape
def draw_symmetric_x(size, lines):
    angle = 360 / lines
    for _ in range(lines):
        pen.color(random_color())
        pen.forward(size)
        pen.backward(size)
        pen.right(angle)

# Draw the X shape
pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_symmetric_x(300, 24)

# Add some humor with turtle's final message
pen.penup()
pen.goto(-200, -350)
pen.color("black")
pen.write("Did you enjoy drawing this X? Turtle did too!", font=("Arial", 16, "normal"))

# Finish
turtle.done()