import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Colorful Symmetric Spiral")

# Setup the turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.width(2)

# Function to generate random color
def random_color():
    return (random.random(), random.random(), random.random())

# Function to draw a symmetric spiral
def draw_symmetric_spiral():
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.pendown()
    
    for i in range(360):
        spiral_turtle.color(random_color())
        spiral_turtle.forward(i * 2)
        spiral_turtle.right(91)

# Create the symmetric spiral
draw_symmetric_spiral()

# Hide the turtle and display the window
spiral_turtle.hideturtle()
turtle.done()