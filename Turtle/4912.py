import turtle
import random

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_mandala():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor('black')
    screen.title('Beautiful Mandala with Python Turtle')

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    turtle.colormode(255)  # Use 255 color mode for RGB

    num_circles = 36
    radius = 150  # Reduced radius to fit within the screen

    # Adjust the starting y-coordinate to center the mandala
    for i in range(num_circles):
        t.color(random_color())
        t.penup()
        t.goto(0, 0)  # Start from the center
        t.pendown()
        t.circle(radius)
        t.right(360 / num_circles)

    for _ in range(6):
        t.color(random_color())
        for _ in range(36):
            t.forward(200)  # Reduced length to fit within the screen
            t.backward(200)
            t.right(10)
        t.right(60)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_mandala()

