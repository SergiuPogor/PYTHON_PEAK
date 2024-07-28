import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("black")
screen.tracer(0)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Function to draw a futuristic table
def draw_table():
    pen.color("white")
    pen.penup()
    pen.goto(-300, -100)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(600)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()

# Function to draw hover-toast
def draw_hover_toast(x, y):
    pen.color("orange")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(100)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(x + 10, y - 10)
    pen.pendown()
    pen.color("yellow")
    pen.circle(20)

# Function to draw levitating eggs
def draw_levitating_eggs(x, y):
    pen.color("white")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    pen.penup()
    pen.goto(x + 5, y + 5)
    pen.color("yellow")
    pen.pendown()
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

# Function to draw neon fruits
def draw_neon_fruit(x, y, color):
    pen.color(color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

# Drawing the scene
draw_table()
draw_hover_toast(-250, -50)
draw_levitating_eggs(-100, 0)
draw_neon_fruit(50, 50, "lime")
draw_neon_fruit(150, -20, "hot pink")

# Finalize the drawing
screen.update()
turtle.done()

