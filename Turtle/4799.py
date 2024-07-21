
import turtle
import random


# Setup Turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.setup(width=800, height=800)
turtle.colormode(255)  # Set color mode to 255 to use RGB values


# Function to draw a colorful shape
def draw_shape(size, sides):
    for _ in range(sides):
        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.forward(size)
        turtle.right(360 / sides)


# Draw symmetric pattern
num_shapes = 12
shape_size = 200
for _ in range(num_shapes):
    draw_shape(shape_size, 6)
    turtle.right(360 / num_shapes)

# Hide Turtle and display final image
turtle.hideturtle()
turtle.done()

