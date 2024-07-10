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

# Constants for boundaries
BOUNDARY = 500


def random_color():
    return (random.random(), random.random(), random.random())


def is_within_bounds(x, y, boundary):
    return -boundary < x < boundary and -boundary < y < boundary


def draw_pattern(t, num_patterns, step_size):
    for i in range(num_patterns):
        t.color(random_color())
        t.begin_fill()
        for _ in range(4):
            t.forward(step_size)
            t.left(90)
            t.forward(step_size)
            t.right(90)
        t.end_fill()
        t.right(360 / num_patterns + random.randint(0, 5))
        t.penup()
        t.forward(step_size + random.randint(0, 50))
        t.pendown()

        # Boundary check
        if not is_within_bounds(t.xcor(), t.ycor(), BOUNDARY):
            t.penup()
            t.goto(0, 0)
            t.pendown()


# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw patterns
draw_pattern(t, 36, 50)

# Finish
turtle.done()

