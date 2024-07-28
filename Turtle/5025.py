import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("skyblue")
screen.tracer(1)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Draw the tree trunk
def draw_trunk():
    pen.color("saddlebrown")
    pen.begin_fill()
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.setheading(90)
    pen.forward(300)
    pen.right(30)
    pen.forward(50)
    pen.right(120)
    pen.forward(100)
    pen.right(120)
    pen.forward(50)
    pen.end_fill()

# Draw branches with leaves
def draw_branch(length, angle):
    if length > 10:
        pen.forward(length)
        pen.right(angle)
        draw_branch(length - 15, angle)
        pen.left(2 * angle)
        draw_branch(length - 15, angle)
        pen.right(angle)
        pen.backward(length)
    else:
        # Draw leaves at the end of branches
        pen.color("green")
        pen.begin_fill()
        pen.circle(random.randint(5, 10))
        pen.end_fill()

# Draw the entire tree with branches and leaves
def draw_tree():
    draw_trunk()
    pen.color("saddlebrown")
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.setheading(90)
    draw_branch(100, 30)

# Draw the artwork
draw_tree()

# Update the screen and wait
screen.update()
turtle.done()

