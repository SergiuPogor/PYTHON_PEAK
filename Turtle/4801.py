import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor((random.random(), random.random(), random.random()))

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)

# Helper function to draw rectangle
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Draw the iPhone body
body_color = (random.random(), random.random(), random.random())
draw_rectangle(-150, 200, 300, 600, body_color)

# Draw the screen
screen_color = (random.random(), random.random(), random.random())
draw_rectangle(-130, 180, 260, 560, screen_color)

# Draw the home button
pen.penup()
pen.goto(0, -250)
pen.pendown()
pen.color((random.random(), random.random(), random.random()))
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Draw the front camera
pen.penup()
pen.goto(0, 180)
pen.pendown()
pen.color((random.random(), random.random(), random.random()))
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# Draw the speaker
pen.penup()
pen.goto(-50, 200)
pen.pendown()
pen.color((random.random(), random.random(), random.random()))
pen.begin_fill()
pen.forward(100)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.end_fill()

# Draw the volume buttons
for y in range(120, 60, -30):
    draw_rectangle(-160, y, 10, 20, (random.random(), random.random(), random.random()))

# Draw the power button
draw_rectangle(150, 120, 10, 60, (random.random(), random.random(), random.random()))

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()