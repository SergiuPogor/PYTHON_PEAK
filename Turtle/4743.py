import turtle
import random

# Setup turtle screen
screen = turtle.Screen()

screen.bgcolor("black")

# Create turtle object
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Function to draw a complex geometric pattern
def draw_pattern():
    for _ in range(72):
        t.pencolor(random.random(), random.random(), random.random())
        for _ in range(6):
            t.forward(100)
            t.right(60)
        t.right(5)

# Main function to execute drawing
if __name__ == "__main__":
    t.penup()
    t.pendown()
    draw_pattern()
    turtle.done()
