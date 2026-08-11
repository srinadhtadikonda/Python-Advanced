import turtle
import math

screen = turtle.Screen()
screen.setup(700, 700)

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

# Main wheel
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.circle(200)

# Center
pen.penup()
pen.goto(0, 0)
pen.dot(20)

# Spokes
for angle in range(0, 360, 30):

    x = 200 * math.cos(math.radians(angle))
    y = 200 * math.sin(math.radians(angle))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(x, y)

    # Cabin
    pen.penup()
    pen.goto(x - 15, y - 15)
    pen.pendown()
    pen.circle(15)

turtle.done()
