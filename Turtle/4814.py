import turtle
import random

def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_monkey_face():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()

    # Draw face
    draw_circle(t, 0, 0, 200, random_color())

    # Draw eyes
    draw_circle(t, -70, 100, 40, random_color())
    draw_circle(t, 70, 100, 40, random_color())
    draw_circle(t, -70, 120, 20, random_color())
    draw_circle(t, 70, 120, 20, random_color())

    # Draw nose
    draw_circle(t, 0, 50, 30, random_color())

    # Draw mouth
    t.penup()
    t.goto(-60, -50)
    t.pendown()

    t.color(random_color())
    t.right(90)
    t.circle(60, 180)

    # Draw ears closer to the head
    draw_circle(t, -110, 220, 70, random_color())
    draw_circle(t, 270, 220, 70, random_color())

    screen.mainloop()


def random_color():
    return (random.random(), random.random(), random.random())


if __name__ == "__main__":
    draw_monkey_face()

