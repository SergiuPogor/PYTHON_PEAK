import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw a spiral star pattern
def draw_spiral_star(radius, angle):
    for i in range(360):
        color = (random.random(), random.random(), random.random())
        pen.pencolor(color)
        pen.forward(radius)
        pen.left(angle)
        radius += 0.1

# Draw multiple spiral stars
def draw_multiple_spirals():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.width(2)
    for _ in range(10):
        draw_spiral_star(random.randint(10, 150), random.randint(30, 60))
        pen.right(36)

# Execute drawing
draw_multiple_spirals()

# Keep the window open
turtle.done()