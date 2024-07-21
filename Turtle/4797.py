import turtle
import random

# Helper function to convert RGB to normalized values
def rgb_to_normalized(r, g, b):
    return r / 255, g / 255, b / 255


def draw_house():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()

    # Draw the main structure (house)
    t.penup()
    t.goto(-100, -100)  # Position to start drawing the house
    t.pendown()
    t.color(rgb_to_normalized(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    # Draw the roof
    t.penup()
    t.goto(-120, 100)  # Position to start drawing the roof
    t.pendown()
    t.color(rgb_to_normalized(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    t.goto(0, 200)
    t.goto(120, 100)
    t.goto(-120, 100)
    t.end_fill()

    # Draw the chimney
    draw_chimney(t, 0, 200)  # Chimney positioned correctly on the roof

    # Draw windows
    draw_window(t, -80, 10, 40)  # Centered and sized window
    draw_window(t, 40, 10, 40)  # Centered and sized window

    # Draw window details
    draw_window_details(t, -80, -30, 40)  # Centered and sized window details
    draw_window_details(t, 40, -30, 40)  # Centered and sized window details

    # Draw door
    draw_door(t, -30, -100)

    # Draw door details
    draw_door_details(t, -30, -100)

    screen.mainloop()


def draw_window(t, x, y, window_size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(rgb_to_normalized(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    for _ in range(4):
        t.forward(window_size)
        t.right(90)
    t.end_fill()


def draw_window_details(t, x, y, window_size):
    # Move to the center of the window for drawing panes
    t.penup()
    t.goto(x + window_size / 2, y + window_size / 2)
    t.pendown()
    t.color(rgb_to_normalized(0, 0, 0))  # Black color for window details
    t.width(2)

    # Draw vertical pane
    t.penup()
    t.goto(x + window_size / 2, y)
    t.pendown()
    t.goto(x + window_size / 2, y + window_size)

    # Draw horizontal pane
    t.penup()
    t.goto(x, y + window_size / 2)
    t.pendown()
    t.goto(x + window_size, y + window_size / 2)


def draw_door(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(rgb_to_normalized(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    t.goto(x + 60, y)
    t.goto(x + 60, y + 80)
    t.goto(x, y + 80)
    t.goto(x, y)
    t.end_fill()


def draw_door_details(t, x, y):
    t.penup()
    t.goto(x + 30, y + 10)
    t.pendown()
    t.color(rgb_to_normalized(0, 0, 0))  # Black color for door details
    t.width(2)
    # Draw door handle
    t.color(rgb_to_normalized(255, 215, 0))  # Gold color for handle
    t.begin_fill()
    t.circle(5)
    t.end_fill()


def draw_chimney(t, x, y):
    t.penup()
    t.goto(x - 10, y)  # Center the chimney on the roof
    t.pendown()
    t.color(rgb_to_normalized(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.begin_fill()
    t.goto(x + 10, y)
    t.goto(x + 10, y + 50)
    t.goto(x - 10, y + 50)
    t.goto(x - 10, y)
    t.end_fill()

    # Draw chimney smoke
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.color(rgb_to_normalized(192, 192, 192))  # Gray color for smoke
    for _ in range(5):
        t.begin_fill()
        t.circle(random.randint(5, 15))
        t.end_fill()
        t.penup()
        t.goto(x, y + 50 + random.randint(10, 30))
        t.pendown()


# Example usage:
draw_house()

