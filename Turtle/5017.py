import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor('black')

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest speed
spiral.width(2)
spiral.hideturtle()  # Hide the turtle icon

# Center coordinates
center_x, center_y = 0, 0

# Spiral parameters
num_turns = 100
angle_step = 15
radius_step = 5

# Draw the 3D spiral illusion
for i in range(num_turns):
    spiral.penup()
    spiral.goto(center_x, center_y)
    spiral.pendown()
    
    # Generate random color
    color = (random.random(), random.random(), random.random())
    spiral.pencolor(color)
    
    # Draw one segment of the spiral
    spiral.setheading(i * angle_step)
    spiral.forward(radius_step * i)
    spiral.right(90)
    spiral.circle(radius_step * i, 180)
    
    # Move back to center
    spiral.penup()
    spiral.goto(center_x, center_y)
    spiral.pendown()

# Keep the window open until clicked
screen.exitonclick()