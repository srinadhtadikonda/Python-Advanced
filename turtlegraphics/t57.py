import turtle

pen = turtle.Turtle()
pen.speed(0)

# Rocket body
pen.color("gray")
pen.begin_fill()

for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(200)
    pen.left(90)

pen.end_fill()

# Nose
pen.color("red")
pen.begin_fill()

pen.goto(0, 200)
pen.goto(40, 260)
pen.goto(80, 200)

pen.end_fill()

# Window
pen.penup()
pen.goto(25, 140)
pen.pendown()

pen.color("blue")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Flame
pen.penup()
pen.goto(20, 0)
pen.pendown()

pen.color("orange")
pen.begin_fill()

pen.goto(40, -70)
pen.goto(60, 0)
pen.goto(40, -40)
pen.goto(20, 0)

pen.end_fill()

turtle.done()
