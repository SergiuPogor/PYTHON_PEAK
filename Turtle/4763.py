import turtle
import random

# Setup turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

def random_color():
    return (random.random(), random.random(), random.random())

def draw_shape(t, length, depth):
    if depth == 0:
        return
    t.color(random_color())
    for _ in range(6):
        t.forward(length)
        t.right(60)
        draw_shape(t, length / 2, depth - 1)

def draw_pattern(t, length, depth):
    for _ in range(36):
        draw_shape(t, length, depth)
        t.right(10)

# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw geometric patterns
draw_pattern(t, 200, 4)

# Finish
turtle.done()