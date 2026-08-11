import turtle

pen = turtle.Turtle()
pen.speed(0)

# Signal box
pen.penup()
pen.goto(-60, -180)
pen.pendown()

pen.color("black")
pen.begin_fill()

for i in range(2):
    pen.forward(120)
    pen.left(90)
    pen.forward(360)
    pen.left(90)

pen.end_fill()

# Red
pen.penup()
pen.goto(0, 100)
pen.pendown()

pen.color("red")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Yellow
pen.penup()
pen.goto(0, 0)
pen.pendown()

pen.color("yellow")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Green
pen.penup()
pen.goto(0, -100)
pen.pendown()

pen.color("green")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

turtle.done()
