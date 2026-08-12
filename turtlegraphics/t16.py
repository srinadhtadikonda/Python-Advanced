#house
import turtle

pen = turtle.Turtle()
pen.speed(3)

# House body
pen.color("blue")
pen.begin_fill()

for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.end_fill()

# Roof
pen.color("red")
pen.begin_fill()

pen.goto(0, 200)
pen.goto(100, 300)
pen.goto(200, 200)

pen.end_fill()

# Door
pen.penup()
pen.goto(75, 0)
pen.pendown()

pen.color("brown")
pen.begin_fill()

for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)

pen.end_fill()

turtle.done()
