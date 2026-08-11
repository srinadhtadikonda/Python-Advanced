import turtle

pen = turtle.Turtle()
pen.speed(3)
pen.color("red")

pen.begin_fill()

pen.left(140)
pen.forward(180)

pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)

pen.forward(180)

pen.end_fill()

turtle.done()
