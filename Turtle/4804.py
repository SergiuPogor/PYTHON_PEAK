import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Turtle setup
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
turtle.colormode(255)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_spiral():
    for i in range(360):
        spiral.color(random_color())
        spiral.forward(i * 2)
        spiral.right(59)  # Angle for the spiral effect

def main():
    spiral.penup()
    spiral.goto(0, 0)
    spiral.pendown()
    draw_spiral()
    spiral.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
