# Import the turtle module
import turtle

# Forming the window screen
tut = turtle.Screen()

# Background color green
tut.bgcolor("green")

# Window title
tut.title("3D Cuboid using Turtle")

# Create turtle object
my_pen = turtle.Turtle()

# Object color
my_pen.color("orange")
my_pen.pensize(3)

# Forming front rectangle face
for i in range(2):
    my_pen.forward(100)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)

# Bottom left side
my_pen.goto(50, 50)

# Forming back rectangle face
for i in range(2):
    my_pen.forward(100)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)

# Bottom right side
my_pen.goto(150, 50)
my_pen.goto(100, 0)

# Top right side
my_pen.goto(100, 150)
my_pen.goto(150, 200)

# Top left side
my_pen.goto(50, 200)
my_pen.goto(0, 150)

# Return to starting point
my_pen.goto(0, 0)

# Hide turtle
my_pen.hideturtle()

# Keep the window open
turtle.done()
