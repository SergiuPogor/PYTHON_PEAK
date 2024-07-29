import turtle
import random

# Set up the screen with the given size
screen = turtle.Screen()
screen.setup(width=1920, height=1080)

# Create a turtle named "artist" with a specific shape
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed

# Move the turtle to the center for symmetry
artist.penup()
artist.goto(0, 0)
artist.pendown()

# Define a function to draw a spiral with random colors
def draw_colorful_spiral(t, size):
    angle = 59  # Spiral angle
    for i in range(size):
        # Set random RGB colors
        t.color(random.random(), random.random(), random.random())
        t.forward(i * 10)  # Increase step size
        t.right(angle)

# Let's draw something spectacular!
draw_colorful_spiral(artist, 100)

# Hide the turtle after drawing
artist.hideturtle()

# Keep the window open until clicked
screen.exitonclick()