import turtle
import random

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_network_diagram():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor("black")
    screen.title("Home Network Diagram")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.width(2)

    # Draw the central server
    artist.penup()
    artist.goto(0, 0)
    artist.pendown()
    color = random_color()
    artist.pencolor(color)
    artist.fillcolor(color)
    artist.begin_fill()
    artist.circle(50)
    artist.end_fill()

    # Draw connected devices
    for i in range(6):
        angle = i * 60
        artist.penup()
        artist.goto(0, 0)
        artist.setheading(angle)
        artist.forward(150)
        artist.pendown()
        color = random_color()
        artist.pencolor(color)
        artist.fillcolor(color)
        artist.begin_fill()
        artist.circle(30)
        artist.end_fill()

        # Draw connections
        artist.penup()
        artist.goto(0, 0)
        artist.pendown()
        artist.pencolor(random_color())
        artist.setheading(angle)
        artist.forward(150)
        artist.right(90)
        artist.forward(15)
        artist.backward(30)
        artist.forward(15)
        artist.left(90)

    artist.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_network_diagram()
