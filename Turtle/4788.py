import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

turtle.speed(0)
turtle.hideturtle()

def draw_network_diagram(size):
    colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33F0", "#33FFF3", "#F033FF"]
    
    for _ in range(size):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        
        for _ in range(6):
            turtle.color(random.choice(colors))
            turtle.forward(50)
            turtle.right(60)

draw_network_diagram(100)

turtle.done()
