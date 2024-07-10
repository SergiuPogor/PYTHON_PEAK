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


def draw_fractal(t, length, depth):
    if depth == 0:
        return
    t.color(random_color())
    t.forward(length)
    t.left(45)
    draw_fractal(t, length * 0.7, depth - 1)
    t.right(90)
    draw_fractal(t, length * 0.7, depth - 1)
    t.left(45)
    t.backward(length)


def draw_pattern(t, depth):
    for i in range(12):
        draw_fractal(t, 100, depth)
        t.right(30)


# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw fractal patterns
draw_pattern(t, 5)

# Finish
turtle.done()

