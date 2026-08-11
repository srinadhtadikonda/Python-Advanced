import turtle

pen = turtle.Turtle()
pen.speed(0)

def koch(length, level):

    if level == 0:
        pen.forward(length)
        return

    length = length / 3

    koch(length, level - 1)

    pen.left(60)
    koch(length, level - 1)

    pen.right(120)
    koch(length, level - 1)

    pen.left(60)
    koch(length, level - 1)


for i in range(3):
    koch(300, 3)
    pen.right(120)

turtle.done()
