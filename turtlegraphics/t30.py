import turtle

t = turtle.Turtle()
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

turtle.done()
