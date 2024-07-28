import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor('black')

# Create a turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.width(2)
artist.hideturtle()

# Center coordinates
center_x, center_y = 0, 0

# Hypocycloid parameters
R = 300  # Radius of the larger circle
r = 100  # Radius of the smaller circle
d = 200  # Distance from the center of the smaller circle to the tracing point

# Number of steps for the pattern
steps = 360

# Draw the hypocycloid pattern
for i in range(steps):
    t = math.radians(i)
    x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
    
    artist.penup()
    artist.goto(center_x + x, center_y + y)
    artist.pendown()
    
    # Generate random color
    color = (random.random(), random.random(), random.random())
    artist.pencolor(color)
    
    # Draw the point
    artist.dot(4)

# Keep the window open until clicked
screen.exitonclick()
