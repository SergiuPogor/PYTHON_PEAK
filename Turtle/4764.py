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

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)
        
def draw_symmetric_pattern(t, size, depth):
    if depth == 0:
        return
    t.color(random_color())
    for _ in range(36):
        draw_star(t, size)
        t.right(10)
    draw_symmetric_pattern(t, size/1.5, depth-1)

# Move turtle to starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw geometric patterns
draw_symmetric_pattern(t, 300, 4)

# Finish
turtle.done()