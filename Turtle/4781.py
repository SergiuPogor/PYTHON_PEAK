import turtle
import random

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_pattern():
    screen = turtle.Screen()
    screen.colormode(255)  # Use 255 to represent full color range
    screen.bgcolor("black")
    screen.title("Unique Python Art")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.width(2)

    # Draw multiple layers of patterns
    for i in range(36):
        color = random_color()
        artist.pencolor(color)
        artist.fillcolor(color)
        artist.begin_fill()

        # Draw a star
        for _ in range(5):
            artist.forward(200)
            artist.right(144)
        artist.end_fill()

        artist.right(10)

    artist.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_pattern()
