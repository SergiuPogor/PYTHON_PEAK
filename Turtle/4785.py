
import random

import turtle as t


# Function to generate a random RGB color
def random_color():
    return (random.random(), random.random(), random.random())


# Function to draw a symmetric X pattern
def draw_x_pattern(size):
    t.speed(0)
    t.width(2)

    for _ in range(4):
        t.color(random_color())
        t.forward(size)
        t.backward(size)
        t.left(90)

    t.penup()
    t.goto(-size // 2, size // 2)
    t.pendown()

    for _ in range(4):
        t.color(random_color())
        t.forward(size)
        t.backward(size)
        t.right(90)

    t.hideturtle()


# Function to draw multiple X patterns
def draw_multiple_patterns(n, max_size):
    for _ in range(n):
        x = random.randint(-max_size // 2, max_size // 2)
        y = random.randint(-max_size // 2, max_size // 2)
        size = random.randint(20, max_size // 4)

        t.penup()
        t.goto(x, y)
        t.pendown()

        draw_x_pattern(size)


# Setting up the screen
t.colormode(1.0)  # Use 1.0 for RGB values
t.setup(width=800, height=800)
t.bgcolor("black")
t.title("Python Turtle X Pattern")

# Drawing multiple X patterns
draw_multiple_patterns(50, 800)

# Ensure the window stays open until manually closed
t.done()

