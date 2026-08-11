import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

text = "WELCOME TO PYTHON"

for color in colors:

    pen.clear()

    pen.color(color)

    pen.penup()
    pen.goto(0, 0)

    pen.write(
        text,
        align="center",
        font=("Arial", 30, "bold")
    )

    time.sleep(0.3)

turtle.done()
