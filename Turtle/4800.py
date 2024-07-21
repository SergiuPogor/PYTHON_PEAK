import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Function to get random color
def get_random_color():
    return (random.random(), random.random(), random.random())

# Draw symmetric pattern
for i in range(36):
    pen.color(get_random_color())
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.seth(i * 10)
    
    for _ in range(36):
        pen.forward(200)
        pen.right(170)

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()