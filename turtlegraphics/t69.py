import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.width(3)

def branch(length):
    if length < 10:
        return

    pen.forward(length)
    pen.backward(length / 3)

    pen.left(45)
    branch(length / 2)
    pen.right(90)
    branch(length / 2)
    pen.left(45)

    pen.backward(length * 2 / 3)

for i in range(6):
    branch(120)
    pen.right(60)

turtle.done()
