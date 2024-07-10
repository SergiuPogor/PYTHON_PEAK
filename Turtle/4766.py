import turtle
import random

def random_color():
    return random.random(), random.random(), random.random()

def draw_shape(t, size, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

def draw_pattern(t, size, depth, sides):
    if depth == 0:
        return
    t.color(random_color())
    for _ in range(36):
        draw_shape(t, size, sides)
        t.right(10)
    draw_pattern(t, size / 1.5, depth - 1, sides + 1)

# Setup turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw geometric patterns
draw_pattern(t, 300, 4, 5)

# Finish
turtle.done()