import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Create the turtle
pie_chart = turtle.Turtle()
pie_chart.speed(0)  # Fastest speed

# Function to generate random color
def random_color():
    return (random.random(), random.random(), random.random())

# Data for the pie chart (values representing different investments)
data = [20, 30, 10, 25, 15]

# Calculate total value and angles
total = sum(data)
angles = [360 * (value / total) for value in data]

# Draw the pie chart
start_angle = 0
for angle in angles:
    pie_chart.color(random_color())
    pie_chart.begin_fill()
    pie_chart.setheading(start_angle)
    pie_chart.forward(100)
    pie_chart.left(90)
    pie_chart.circle(100, angle)
    pie_chart.left(90)
    pie_chart.forward(100)
    pie_chart.end_fill()
    
    	start_angle += angle

# Hide the turtle and display the result
pie_chart.hideturtle()
turtle.done()

