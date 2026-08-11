import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["red", "blue", "green", "purple", "orange", "pink"]

for i in range(60):
    pen.color(colors[i % len(colors)])

    for j in range(6):
        pen.circle(50)
        pen.left(60)

    pen.left(6)

turtle.done()
