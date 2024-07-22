import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")

# Create a turtle object
cubicle_turtle = turtle.Turtle()
cubicle_turtle.speed(0)
cubicle_turtle.width(2)

# Generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw a futuristic cubicle pattern
def draw_cubicle(size, angle_step):
    for _ in range(int(360 / angle_step)):
        color = random_color()
        screen.colormode(255)  # Set color mode to 255 for RGB
        cubicle_turtle.pencolor(color)
        for _ in range(4):
            cubicle_turtle.forward(size)
            cubicle_turtle.right(90)
        cubicle_turtle.right(angle_step)

# Center the cubicle pattern on the screen
cubicle_turtle.penup()
cubicle_turtle.goto(0, 0)
cubicle_turtle.pendown()

# Draw multiple cubicle layers
for i in range(5):
    draw_cubicle(100 + i*50, 15)

# Hide the turtle
cubicle_turtle.hideturtle()

# Keep the window open
turtle.done()