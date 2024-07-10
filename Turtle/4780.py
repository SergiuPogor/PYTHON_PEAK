import turtle
import random

# Function to generate a random RGB color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw a nature-inspired pattern
def draw_nature_pattern():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.colormode(255)

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    # Define the number of patterns and steps
    num_patterns = 10
    steps = 36

    # Draw multiple nature-inspired patterns
    for i in range(num_patterns):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.color(random_color())

        angle = 360 / steps
        for _ in range(steps):
            t.forward(200)
            t.right(angle)
            t.circle(50)
            t.right(angle)

        t.right(360 / num_patterns)

    screen.mainloop()

draw_nature_pattern()