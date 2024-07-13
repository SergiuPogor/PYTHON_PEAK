import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Colorful Symmetrical Tree Drawing with Turtle")
screen.bgcolor("white")

# Set up the turtle
tree = turtle.Turtle()
tree.speed(0)  # Fastest drawing speed
tree.hideturtle()
tree.width(2)

# Random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw a tree branch
def draw_branch(length, angle):
    if length < 10:
        return
    tree.color(random_color())
    tree.forward(length)
    tree.left(angle)
    draw_branch(length - random.randint(10, 20), angle)
    tree.right(2 * angle)
    draw_branch(length - random.randint(10, 20), angle)
    tree.left(angle)
    tree.backward(length)

# Initialize turtle and start drawing
turtle.colormode(255)
tree.penup()
tree.goto(0, -300)
tree.pendown()
tree.setheading(90)  # Point turtle upwards

# Draw the tree with multiple branches
draw_branch(100, 30)

# Finish up
turtle.done()