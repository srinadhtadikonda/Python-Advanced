import turtle

# Screen
screen = turtle.Screen()
screen.setup(900, 600)
screen.title("Indian National Flag")

# Turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Function to draw rectangle
def rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.color(color)
    pen.fillcolor(color)

    pen.begin_fill()

    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.end_fill()


# -------------------------
# Flag
# -------------------------

x = -350
width = 700
height = 100

# Saffron
rectangle(x, 100, width, height, "#FF9933")

# White
rectangle(x, 0, width, height, "white")

# Green
rectangle(x, -100, width, height, "#138808")


# -------------------------
# Ashoka Chakra
# -------------------------

pen.penup()
pen.goto(0, -50)
pen.pendown()

pen.color("#000080")
pen.pensize(3)

# Outer circle
pen.circle(50)

# 24 spokes
for i in range(24):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(i * 15)
    pen.pendown()
    pen.forward(50)


# Center circle
pen.penup()
pen.goto(0, -5)
pen.pendown()

pen.begin_fill()
pen.circle(5)
pen.end_fill()


# -------------------------
# Flag Pole
# -------------------------

pen.pensize(8)
pen.color("brown")

pen.penup()
pen.goto(-370, -400)
pen.pendown()
pen.goto(-370, 250)

# Pole top
pen.penup()
pen.goto(-370, 250)
pen.pendown()
pen.dot(20, "gold")


# -------------------------
# Base
# -------------------------

pen.pensize(3)

rectangle(-430, -420, 120, 20, "brown")
rectangle(-410, -400, 80, 20, "brown")


# -------------------------
# Text
# -------------------------

pen.penup()
pen.goto(0, -470)

pen.color("#000080")
pen.write(
    "JAI HIND",
    align="center",
    font=("Arial", 28, "bold")
)

pen.hideturtle()

turtle.done()
