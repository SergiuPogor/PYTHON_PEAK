import turtle
import random

# Initialize the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=1000)

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# List of colors to use in the pattern
colors = ["red", "yellow", "blue", "green", "purple", "orange", "white"]

# Function to draw a polygon with a given number of sides and size
def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Function to draw a star with a given size
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

# Draw multiple patterns
for i in range(150):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-400, 400))
    t.pendown()
    t.color(random.choice(colors))
    
    pattern_type = random.choice(["polygon", "star"])
    if pattern_type == "polygon":
        sides = random.randint(3, 10)
        size = random.randint(20, 100)
        draw_polygon(sides, size)
    else:
        size = random.randint(20, 100)
        draw_star(size)

# Function to draw concentric circles
def draw_circles(radius):
    for _ in range(36):
        t.color(random.choice(colors))
        t.circle(radius)
        t.right(10)

# Draw concentric circles
t.penup()
t.goto(0, 0)
t.pendown()
draw_circles(100)

# Function to draw a spirograph
def draw_spirograph(size):
    for _ in range(72):
        t.color(random.choice(colors))
        t.circle(size)
        t.right(5)

# Draw a spirograph
t.penup()
t.goto(0, -200)
t.pendown()
draw_spirograph(150)

# Keep the window open
turtle.done()