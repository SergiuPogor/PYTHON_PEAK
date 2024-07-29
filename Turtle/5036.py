import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("black")
screen.tracer(1)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Function to draw stars
def draw_star(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        pen.forward(size)
        pen.left(72)
    pen.end_fill()

# Function to draw the galaxy's core
def draw_core():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

# Function to draw spiral arms
def draw_spiral_arms():
    colors = ["blue", "purple", "pink", "cyan", "magenta"]
    for i in range(5):
        pen.color(colors[i % len(colors)])
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.right(144)
        for j in range(120):
            pen.forward(j * 2)
            pen.right(45 + (i * 2))

# Function to add stars
def add_stars():
    for _ in range(50):
        x = random.randint(-960, 960)
        y = random.randint(-540, 540)
        size = random.randint(5, 15)
        color = random.choice(["white", "yellow", "lightblue"])
        draw_star(x, y, size, color)

# Draw the galaxy
draw_core()
draw_spiral_arms()
add_stars()

# Update the screen and finish
screen.update()
turtle.done()
