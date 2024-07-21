import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Create the turtle
flake = turtle.Turtle()
flake.speed(0)
flake.width(2)


# Function to draw a Koch curve
def koch_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(turtle, length, depth - 1)
        turtle.left(60)
        koch_curve(turtle, length, depth - 1)
        turtle.right(120)
        koch_curve(turtle, length, depth - 1)
        turtle.left(60)
        koch_curve(turtle, length, depth - 1)


# Function to draw a complete snowflake
def draw_snowflake(turtle, length, depth):
    for _ in range(3):
        koch_curve(turtle, length, depth)
        turtle.right(120)


# Position the turtle and draw the snowflake
flake.penup()
flake.goto(-300, 150)  # Adjusted starting position
flake.pendown()

# Draw the snowflake
flake.color("blue")
draw_snowflake(flake, 600, 4)  # Adjust length and depth for size and detail

# Hide the turtle and display the window
flake.hideturtle()
turtle.done()

