import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("black")
screen.tracer(1)

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Random color generator
def random_color():
    return (random.random(), random.random(), random.random())

# Draw a single square
def draw_square(size, offset_x=0, offset_y=0, color="white"):
    pen.color(color)
    pen.penup()
    pen.goto(offset_x, offset_y)
    pen.pendown()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Draw a 3D cube
def draw_cube(size, color="white"):
    offset_x = -size / 2
    offset_y = size / 2

    # Draw front face
    draw_square(size, offset_x, offset_y, color=color)

    # Draw back face
    draw_square(size, offset_x + size / 2, offset_y - size / 2, color=color)

    # Connect corresponding corners
    pen.color(color)
    for (start_x, start_y, end_x, end_y) in [(offset_x, offset_y, offset_x + size / 2, offset_y - size / 2),
                                             (offset_x + size, offset_y, offset_x + size + size / 2, offset_y - size / 2),
                                             (offset_x + size, offset_y - size, offset_x + size + size / 2, offset_y - size - size / 2),
                                             (offset_x, offset_y - size, offset_x + size / 2, offset_y - size - size / 2)]:
        pen.penup()
        pen.goto(start_x, start_y)
        pen.pendown()
        pen.goto(end_x, end_y)

# Draw multiple 3D cubes
def draw_multiple_cubes():
    sizes = [400, 300, 200, 150, 100, 50, 30, 20, 10]
    for size in sizes:
        color = random_color()
        draw_cube(size, color=color)

# Draw the cubes
draw_multiple_cubes()

# Update the screen and wait
screen.update()
turtle.done()

