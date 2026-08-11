import turtle

pen = turtle.Turtle()
pen.speed(3)

# Draw box
pen.penup()
pen.goto(-250, -80)
pen.pendown()

pen.color("blue")
pen.pensize(4)

for i in range(2):
    pen.forward(500)
    pen.left(90)
    pen.forward(160)
    pen.left(90)

# Write text
pen.penup()
pen.goto(0, 0)

pen.color("red")
pen.write(
    "PYTHON TURTLE",
    align="center",
    font=("Arial", 30, "bold")
)

pen.goto(0, -45)

pen.color("green")
pen.write(
    "Learn • Create • Explore",
    align="center",
    font=("Arial", 18, "italic")
)

turtle.done()
