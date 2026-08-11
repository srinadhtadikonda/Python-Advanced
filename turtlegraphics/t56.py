import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Sun
pen.penup()
pen.goto(0, -50)
pen.pendown()

pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Planets
planets = [
    (-100, 0, 10, "gray"),
    (-180, 50, 15, "orange"),
    (100, 80, 20, "blue"),
    (180, -80, 18, "red")
]

for x, y, radius, color in planets:

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

turtle.done()
