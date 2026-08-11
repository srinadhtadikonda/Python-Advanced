import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

text = "PYTHON"
colors = ["red", "orange", "green", "blue", "purple", "brown"]

start_x = -150

for i in range(len(text)):
    pen.goto(start_x + i * 50, 0)
    pen.color(colors[i])
    pen.write(
        text[i],
        align="center",
        font=("Arial", 36, "bold")
    )

turtle.done()
