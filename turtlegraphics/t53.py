import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")

# Sun
pen.begin_fill()
pen.circle(80)
pen.end_fill()

# Rays
for i in range(18):
    pen.penup()
    pen.goto(0, 80)
    pen.pendown()
    
    pen.forward(140)
    pen.backward(140)
    pen.right(20)

turtle.done()
