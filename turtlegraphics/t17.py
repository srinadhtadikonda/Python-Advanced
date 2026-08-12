#car
import turtle

pen = turtle.Turtle()
pen.speed(3)

# Car body
pen.color("blue")
pen.begin_fill()

pen.goto(-200, 0)
pen.goto(-120, 80)
pen.goto(80, 80)
pen.goto(160, 0)
pen.goto(200, 0)
pen.goto(200, -80)
pen.goto(-200, -80)
pen.goto(-200, 0)

pen.end_fill()

# Wheels
for x in [-120, 120]:
    pen.penup()
    pen.goto(x, -80)
    pen.pendown()
    
    pen.color("black")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()

turtle.done()
