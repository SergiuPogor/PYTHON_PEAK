import turtle as t
import random

# Setup turtle screen
screen = t.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("white")

# Function to draw complex geometric patterns
def draw_patterns():
    t.speed(0)
    colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#1A1A1D"]
    
    for _ in range(100):
        t.pencolor(random.choice(colors))
        size = random.randint(10, 200)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        t.penup()
        t.goto(x, y)
        t.pendown()
        sides = random.randint(3, 8)
        
        for _ in range(sides):
            t.forward(size)
            t.right(360 / sides)

    t.hideturtle()

# Draw the complex geometric patterns
draw_patterns()

# Keep the window open until manually closed
t.done()