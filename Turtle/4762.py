import random
import turtle

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


def draw_large_spiral(t, length, angle, increment, depth):
    for _ in range(depth):
        t.color(random_color())
        t.forward(length)
        t.right(angle)
        length += increment


# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw large spiral pattern
draw_large_spiral(t, 10, 59, 2, 240)  # Adjust the depth to create a larger pattern

# Finish
turtle.done()

