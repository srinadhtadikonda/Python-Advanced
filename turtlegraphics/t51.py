import turtle
import math

screen = turtle.Screen()
screen.setup(600, 600)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Clock circle
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.circle(200)

# Numbers
for n in range(1, 13):
    angle = math.radians(90 - n * 30)
    x = 165 * math.cos(angle)
    y = 165 * math.sin(angle)

    pen.penup()
    pen.goto(x - 5, y - 10)
    pen.write(str(n), align="center", font=("Arial", 16, "bold"))

turtle.done()
