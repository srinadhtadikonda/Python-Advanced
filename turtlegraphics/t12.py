#import the turtle modules 
import turtle 

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("green")

# window title Turtle
tut.title("Turtle")
my_pen = turtle.Turtle()

# object color
my_pen.color("orange")
tut=turtle.Screen()           

# forming front rectangle face
for i in range(2):
    my_pen.forward(100)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)

# bottom left side
my_pen.goto(50,50)

# forming back rectangle face
for i in range(2):
    my_pen.forward(100)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)

# bottom right side
my_pen.goto(150,50)
my_pen.goto(100,0)

# top right side
my_pen.goto(100,150)
my_pen.goto(150,200)

# top left side
my_pen.goto(50,200)
my_pen.goto(0,150)
