import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")
screen.title("Mesmerizing Geometric Flower Patterns")

# Create the turtle
flower = turtle.Turtle()
flower.speed(0)

# Function to draw a petal
def draw_petal(turtle, radius, angle):
    turtle.color(random.random(), random.random(), random.random())
    turtle.circle(radius, angle)
    turtle.left(180 - angle)
    turtle.circle(radius, angle)
    turtle.left(180 - angle)

# Function to draw the flower
def draw_flower(turtle, num_petals, radius, angle):
    for _ in range(num_petals):
        draw_petal(turtle, radius, angle)
        turtle.left(360 / num_petals)

# Enhanced drawing function to add layers and loops
def draw_complex_flower(turtle, layers, num_petals, radius, angle):
    for layer in range(layers):
        draw_flower(turtle, num_petals, radius, angle)
        turtle.right(10)  # Slight rotation for each layer
        radius -= 10  # Reduce radius for next layer
        if radius <= 0:
            break  # Stop if radius becomes non-positive

# Define parameters for the flower
num_petals = 36
radius = 200
angle = 60
layers = 50

# Position the turtle
flower.penup()
flower.goto(0, 0)
flower.pendown()

# Draw the complex flower
draw_complex_flower(flower, layers, num_petals, radius, angle)

# Hide the turtle
flower.hideturtle()

# Keep the window open
turtle.done()

