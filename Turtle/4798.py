import turtle
import random

def draw_geometric_illusion():
    turtle.speed(0)
    turtle.bgcolor("black")
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    turtle.hideturtle()
    for _ in range(36):
        for _ in range(4):
            turtle.color(random.choice(colors))
            turtle.forward(200)
            turtle.left(90)
        turtle.right(10)

    turtle.done()

draw_geometric_illusion()