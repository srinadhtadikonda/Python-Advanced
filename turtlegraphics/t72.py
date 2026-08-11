import turtle

pen = turtle.Turtle()
pen.hideturtle()

pen.penup()
pen.goto(0, 50)

pen.color("blue")
pen.write(
    "Welcome to Python Turtle",
    align="center",
    font=("Arial", 24, "bold")
)

pen.goto(0, 0)
pen.color("green")
pen.write(
    "Learn Python with Graphics!",
    align="center",
    font=("Arial", 18, "normal")
)

turtle.done()

