import turtle
import math

screen = turtle.Screen()
screen.setup(800, 600)

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

for y in range(-250, 251, 10):

    x = 150 * math.sin(y / 40)

    # Left strand
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(8)

    # Right strand
    pen.penup()
    pen.goto(-x, y)
    pen.pendown()
    pen.dot(8)

    # Connecting line
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(-x, y)

turtle.done()
