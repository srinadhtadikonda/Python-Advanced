import turtle

pen = turtle.Turtle()
pen.speed(0)

def triangle(size, level):

    if level == 0:

        for i in range(3):
            pen.forward(size)
            pen.left(120)

        return

    triangle(size / 2, level - 1)

    pen.forward(size / 2)

    triangle(size / 2, level - 1)

    pen.backward(size / 2)
    pen.left(60)
    pen.forward(size / 2)
    pen.right(60)

    triangle(size / 2, level - 1)

    pen.left(60)
    pen.backward(size / 2)
    pen.right(60)


pen.penup()
pen.goto(-200, -150)
pen.pendown()

triangle(400, 4)

turtle.done()
