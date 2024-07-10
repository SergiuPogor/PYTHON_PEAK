import random
import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.setup(width=1000, height=1000)


def draw_pattern():
    for _ in range(36):
        for _ in range(4):
            turtle.color(random.random(), random.random(), random.random())
            turtle.forward(100)
            turtle.left(90)
        turtle.left(10)


def draw_another_pattern():
    for _ in range(36):
        for _ in range(4):
            turtle.color(random.random(), random.random(), random.random())
            turtle.forward(150)  # Increase the length to add more drawing time
            turtle.right(90)
        turtle.right(10)


draw_pattern()
draw_another_pattern()
turtle.hideturtle()
turtle.done()

