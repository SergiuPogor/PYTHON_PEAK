
import random

import turtle as t

# Function to create a colorful pattern with Python Turtle
def create_colorful_pattern(size, levels):
    t.speed(0)
    t.width(2)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Calculate maximum distance for centering and fitting
    max_distance = 350 / levels

    for level in range(levels):
        angle_shift = level * 10  # Add a shift in angle for each level to avoid overlap
        for i in range(size):
            t.penup()
            t.goto(0, 0)  # Ensure the turtle starts from the center
            t.pendown()
            t.color(random.choice(colors))
            t.right(360 / size + angle_shift)  # Add rotation based on level to avoid overlap
            t.forward(max_distance * (level + 1))
            t.right(45)  # Rotate to add more complexity
            for _ in range(2):
                t.circle(max_distance / 4, 90)  # Draw a quarter-circle
                t.right(90)
            t.right(360 / size)

    t.hideturtle()

# Setting up the screen
t.setup(width=800, height=800)
t.bgcolor("white")
t.title("Efficiency Boost: Colorful Patterns with Python Turtle")

# Drawing the colorful pattern with more levels
create_colorful_pattern(12, 8)

# Ensure the window stays open until manually closed
t.done()

