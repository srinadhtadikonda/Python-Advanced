import turtle

ws = turtle.Screen()
geekyTurtle = turtle.Turtle()

geekyTurtle.speed(3)
geekyTurtle.color("blue")
geekyTurtle.pensize(3)

for i in range(8):
    geekyTurtle.forward(100)
    geekyTurtle.left(45)

turtle.done()
