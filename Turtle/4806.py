import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Turtle setup
garden = turtle.Turtle()
garden.speed(0)
turtle.colormode(255)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_flower(x, y):
    garden.penup()
    garden.goto(x, y)
    garden.pendown()
    for _ in range(36):
        garden.color(random_color())
        garden.circle(50, steps=6)  # Hexagon petals
        garden.right(10)

def draw_leaf(x, y):
    garden.penup()
    garden.goto(x, y)
    garden.pendown()
    garden.color(random_color())
    garden.begin_fill()
    garden.circle(40, 90)
    garden.left(90)
    garden.circle(40, 90)
    garden.end_fill()

def draw_garden():
    for _ in range(10):
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        draw_flower(x, y)
        draw_leaf(x + random.randint(-50, 50), y + random.randint(-50, 50))

def main():
    draw_garden()
    garden.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
