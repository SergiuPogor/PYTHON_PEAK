import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("sky blue")

# Create a turtle object
bubble_turtle = turtle.Turtle()
bubble_turtle.speed(0)
bubble_turtle.hideturtle()

# Function to generate random colors
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Function to draw a bubble
def draw_bubble(x, y, size):
    bubble_turtle.penup()
    bubble_turtle.goto(x, y)
    bubble_turtle.pendown()
    bubble_turtle.begin_fill()
    bubble_turtle.color(random_color())
    bubble_turtle.circle(size)
    bubble_turtle.end_fill()

# Draw multiple bubbles
for _ in range(50):
    x = random.randint(-900, 900)
    y = random.randint(-500, 500)
    size = random.randint(20, 100)
    draw_bubble(x, y, size)

# Keep the window open
turtle.done()