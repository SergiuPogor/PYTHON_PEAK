import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("white")

# Create a turtle object
gift_turtle = turtle.Turtle()
gift_turtle.speed(0)
gift_turtle.width(3)


# Function to generate random colors
# Function to generate random colors
def random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    return (r, g, b)


# Function to draw a heart
def draw_heart(x, y):
    gift_turtle.penup()
    gift_turtle.goto(x, y)
    gift_turtle.pendown()
    gift_turtle.begin_fill()
    gift_turtle.color(random_color())

    gift_turtle.left(140)
    gift_turtle.forward(180)

    gift_turtle.circle(-90, 200)
    gift_turtle.left(120)
    gift_turtle.circle(-90, 200)

    gift_turtle.forward(180)

    gift_turtle.end_fill()
    gift_turtle.setheading(0)  # Reset heading to default (facing right)


# Function to draw a gift box
def draw_gift_box(x, y):
    gift_turtle.penup()
    gift_turtle.goto(x, y)
    gift_turtle.pendown()
    gift_turtle.begin_fill()
    gift_turtle.color(random_color())
    for _ in range(4):
        gift_turtle.forward(100)
        gift_turtle.right(90)
    gift_turtle.end_fill()

    # Draw ribbon
    gift_turtle.penup()
    gift_turtle.goto(x, y + 100)
    gift_turtle.pendown()
    gift_turtle.width(5)
    gift_turtle.color("red")
    gift_turtle.forward(100)
    gift_turtle.right(90)
    gift_turtle.forward(100)
    gift_turtle.right(90)
    gift_turtle.forward(100)
    gift_turtle.right(90)
    gift_turtle.forward(100)


# Draw multiple hearts and gift boxes
for i in range(-600, 600, 200):
    draw_heart(i, 0)

for i in range(-600, 600, 200):
    draw_gift_box(i, -200)

# Hide the turtle
gift_turtle.hideturtle()

# Keep the window open
turtle.done()

