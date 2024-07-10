import turtle
import random

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_melodyminder():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor("black")
    screen.title("Artistic MelodyMinder Pattern")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.width(2)

    # Draw the MelodyMinder pattern
    for i in range(36):
        color = random_color()
        artist.pencolor(color)
        artist.fillcolor(color)
        artist.begin_fill()

        # Draw a complex shape
        for j in range(8):
            artist.forward(150)
            artist.left(45)
            artist.forward(75)
            artist.right(90)
        
        artist.end_fill()
        artist.right(10)

    artist.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_melodyminder()
