import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Colorful Geometric Flower")

# Setup the turtle
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)
flower_turtle.width(2)


# Function to generate random color
def random_color():
    return (random.random(), random.random(), random.random())


# Draw a single geometric flower
def draw_single_flower(petal_length):
    num_petals = 36
    angle = 360 / num_petals

    for _ in range(num_petals):
        flower_turtle.color(random_color())
        flower_turtle.circle(petal_length, steps=6)
        flower_turtle.right(angle)


# Draw multiple levels of geometric flowers
def draw_flower():
    levels = 3  # Number of levels
    base_length = 150  # Base petal length

    for level in range(levels):
        petal_length = base_length - (level * 50)  # Reduce petal length for each level
        draw_single_flower(petal_length)
        flower_turtle.penup()
        flower_turtle.goto(0, 0)
        flower_turtle.pendown()


# Center the drawing
flower_turtle.penup()
flower_turtle.goto(0, 0)  # Adjusted to center the flower
flower_turtle.pendown()

# Create the flower
draw_flower()

# Hide the turtle and display the window
flower_turtle.hideturtle()
turtle.done()

