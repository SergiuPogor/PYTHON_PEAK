import turtle
import random 
   
# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")

# Create a turtle object
reduce_turtle = turtle.Turtle()
reduce_turtle.speed(0)
reduce_turtle.width(2)


# Generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Draw a pattern representing array reduce use cases
def draw_pattern(size, angle_step):
    for _ in range(int(360 / angle_step)):
        color = random_color()
        screen.colormode(255)  # Set color mode to 255 for RGB
        reduce_turtle.pencolor(color)
        reduce_turtle.forward(size)
        reduce_turtle.right(angle_step)


# Center the pattern on the screen
reduce_turtle.penup()
reduce_turtle.goto(0, 400)
reduce_turtle.pendown()

# Draw multiple patterns
for i in range(50):
    draw_pattern(10 + i * 3, 15)

# Hide the turtle
reduce_turtle.hideturtle()

# Keep the window open
turtle.done()

