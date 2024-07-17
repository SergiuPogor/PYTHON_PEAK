import turtle
import random

def draw_fractal(x, y, size, depth):
    if depth == 0:
        return
    colors = [
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    ]
    turtle.pencolor(colors[depth % 3])
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        draw_fractal(turtle.xcor(), turtle.ycor(), size / 2, depth - 1)
        turtle.left(90)

def main():
    screen = turtle.Screen()
    screen.colormode(255)
    turtle.speed(0)
    turtle.hideturtle()
    draw_fractal(0, 0, 200, 5)
    screen.exitonclick()

if __name__ == "__main__":
    main()