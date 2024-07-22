import turtle
import random

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
turtle.colormode(255)

# Create turtle object
pen = turtle.Turtle()
pen.speed(2)

# Draw car body
pen.penup()
pen.goto(-150, -50)
pen.pendown()
pen.color(random_color())
pen.begin_fill()
pen.forward(300)  # Length of the car body
pen.left(90)
pen.forward(50)  # Height of the car body
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

# Draw car roof
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.color(random_color())
pen.begin_fill()
pen.setheading(0)
pen.forward(200)  # Length of the roof
pen.left(90)
pen.forward(50)  # Height of the roof
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

# Draw windows
pen.penup()
pen.goto(-80, 10)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.setheading(0)
pen.forward(60)  # Width of the window
pen.left(90)
pen.forward(30)  # Height of the window
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(30)
pen.end_fill()

pen.penup()
pen.goto(20, 10)
pen.pendown()
pen.begin_fill()
pen.setheading(0)
pen.forward(60)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(30)
pen.end_fill()

# Draw wheels
for wheel in [(-100, -75), (50, -75)]:
    pen.penup()
    pen.goto(wheel)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(25)  # Radius of the wheel
    pen.end_fill()

# Draw wheel rims
pen.color(random_color())
for rim in [(-100, -75), (50, -75)]:
    pen.penup()
    pen.goto(rim)
    pen.pendown()
    pen.begin_fill()
    pen.circle(15)  # Radius of the rim
    pen.end_fill()

# Hide turtle and display the drawing
pen.hideturtle()
turtle.done()

