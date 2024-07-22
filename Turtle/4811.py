import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('lightblue')

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw a stone
def draw_stone(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random())
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

# Function to draw ripples
def draw_ripples(x, y, size):
    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random())
    pen.width(2)
    for i in range(6):
        pen.circle(size + i * 10)
        pen.penup()
        pen.goto(x, y - size - (i + 1) * 5)
        pen.pendown()

# Draw stones
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(20, 50)
    draw_stone(x, y, size)

# Draw ripples
for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(20, 50)
    draw_ripples(x, y, size)

# Keep the window open
turtle.done()