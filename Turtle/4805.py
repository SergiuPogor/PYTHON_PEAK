import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("white")

# Turtle setup
breath = turtle.Turtle()
breath.speed(0)
breath.width(2)
turtle.colormode(255)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_breathing_animation():
    breath.penup()
    breath.goto(0, -100)  # Adjust starting position
    breath.pendown()

    max_radius = 200  # Maximum radius for the hexagon
    increment = 4  # Increment for expanding hexagons
    steps = 50  # Number of hexagons

    for i in range(steps):
        breath.color(random_color())
        current_radius = max_radius - (steps - i - 1) * increment  # Calculate current radius
        breath.circle(current_radius, steps=6)  # Draw hexagon with current radius
        breath.right(36)  # Rotate for symmetry


def main():
    draw_breathing_animation()
    breath.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

