import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.fillcolor("yellow")

pen.begin_fill()

pen.circle(100, 300)

pen.left(30)
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.end_fill()

# Eye
pen.penup()
pen.goto(30, 70)
pen.pendown()

pen.color("black")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# Food
for x in [180, 230, 280]:

    pen.penup()
    pen.goto(x, 0)
    pen.pendown()

    pen.color("red")
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()

turtle.done()
