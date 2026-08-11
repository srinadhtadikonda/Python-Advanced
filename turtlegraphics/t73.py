import turtle

pen = turtle.Turtle()
pen.hideturtle()

pen.penup()
pen.goto(0, 100)

pen.color("purple")
pen.write(
    "STUDENT PROFILE",
    align="center",
    font=("Arial", 28, "bold")
)

pen.goto(0, 40)
pen.color("blue")
pen.write(
    "Name : Srinadh",
    align="center",
    font=("Arial", 20, "normal")
)

pen.goto(0, 0)
pen.write(
    "Course : Python Programming",
    align="center",
    font=("Arial", 20, "normal")
)

pen.goto(0, -40)
pen.write(
    "Topic : Turtle Graphics",
    align="center",
    font=("Arial", 20, "normal")
)

turtle.done()
