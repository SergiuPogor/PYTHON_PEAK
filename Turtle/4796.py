import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Create a turtle object
bot = turtle.Turtle()
bot.speed(0)
bot.pensize(2)

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Function to draw a symmetric part of the robot
def draw_symmetric_part(size):
    bot.color(random_color())
    for _ in range(4):
        bot.forward(size)
        bot.right(90)
    bot.right(90)
    bot.forward(size)
    bot.left(90)

# Function to draw the robot
def draw_robot():
    bot.penup()
    bot.goto(-50, 50)
    bot.pendown()
    
    # Draw the head
    bot.begin_fill()
    draw_symmetric_part(100)
    bot.end_fill()

    # Draw the eyes
    for i in [-25, 25]:
        bot.penup()
        bot.goto(i, 75)
        bot.pendown()
        bot.begin_fill()
        bot.circle(10)
        bot.end_fill()

    # Draw the body
    bot.penup()
    bot.goto(-50, 0)
    bot.pendown()
    bot.begin_fill()
    draw_symmetric_part(100)
    bot.end_fill()

    # Draw the arms
    for i in [-75, 75]:
        bot.penup()
        bot.goto(i, 25)
        bot.pendown()
        bot.begin_fill()
        draw_symmetric_part(50)
        bot.end_fill()

    # Draw the legs
    for i in [-50, 50]:
        bot.penup()
        bot.goto(i, -100)
        bot.pendown()
        bot.begin_fill()
        draw_symmetric_part(50)
        bot.end_fill()

# Draw the robot with humor!
bot.penup()
bot.goto(0, 150)
bot.write("Meet Bot, the Colorful Robot!", align="center", font=("Arial", 24, "normal"))
bot.hideturtle()

# Start drawing
draw_robot()

# Finish up
turtle.done()