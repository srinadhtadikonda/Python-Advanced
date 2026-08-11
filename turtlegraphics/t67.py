import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

pen.color("purple")

# Left wing
pen.begin_fill()
for i in range(2):
    pen.circle(80, 60)
    pen.left(120)
pen.end_fill()

# Right wing
pen.begin_fill()
for i in range(2):
    pen.circle(-80, 60)
    pen.right(120)
pen.end_fill()

# Body
pen.color("black")
pen.width(8)

pen.penup()
pen.goto(0, -70)
pen.pendown()
pen.goto(0, 70)

# Antenna
pen.width(2)

pen.penup()
pen.goto(0, 70)
pen.pendown()

pen.left(30)
pen.forward(50)
pen.backward(50)

pen.right(60)
pen.forward(50)

turtle.done()
