import turtle
import random

def draw_triangle(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        size /= 2
        draw_triangle(t, order - 1, size)
        t.forward(size)
        draw_triangle(t, order - 1, size)
        t.backward(size)
        t.left(60)
        t.forward(size)
        t.right(60)
        draw_triangle(t, order - 1, size)
        t.left(60)
        t.backward(size)
        t.right(60)

def main():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    order = 4  # Change this for different levels of detail
    
    for _ in range(50):  # Draw multiple triangles with random colors
        t.penup()
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        t.goto(x, y)
        t.pendown()
        
        r = random.random()
        g = random.random()
        b = random.random()
        t.pencolor(r, g, b)
        
        draw_triangle(t, order, 300)
    
    screen.mainloop()

if __name__ == "__main__":
    main()