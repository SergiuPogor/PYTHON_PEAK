import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('darkblue')

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw coral
def draw_coral(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random())
    pen.begin_fill()
    for _ in range(6):
        pen.forward(size)
        pen.right(60)
    pen.end_fill()

# Function to draw fish
def draw_fish(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random())
    pen.begin_fill()
    pen.circle(20, 180)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.circle(20, 180)
    pen.end_fill()

# Function to draw seaweed
def draw_seaweed(x, y, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random())
    pen.width(4)
    pen.left(90)
    pen.forward(height)
    pen.right(90)

# Draw corals
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(20, 50)
    draw_coral(x, y, size)

# Draw fish
for _ in range(6):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw_fish(x, y)

# Draw seaweeds
for _ in range(8):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    height = random.randint(50, 150)
    draw_seaweed(x, y, height)

# Keep the window open
turtle.done()