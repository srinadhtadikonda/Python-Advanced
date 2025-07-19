# importing libraries
import turtle
import random


# creating turtle object
t = turtle.Turtle()

# to activate turtle graphics Screen
w = turtle.Screen()

# setting speed of turtle
t.speed(0)

# giving the background color of turtle
# graphics screen
w.bgcolor("black")

# giving the color of pen to our turtle
# for drawing
t.color("white")

# giving title to our turtle graphics window
w.title("Starry Sky")

# making function to draw the stars
def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)


# loop for making number of stars
for i in range(100):
  
    # generating random integer values for x and y
    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
    
    # calling the function stars to draw the 
    # stars at random x,y value
    stars()
    
    # took up the turtle's pen
    t.up()
    
    # go at the x,y coordinate generated above
    t.goto(x, y)
    
    # took down the pen to draw
    t.down()

# for making our moon looking up the pen
t.up()

# going at the specific coordinated
t.goto(0, 170)

# took down the pen to start drawing
t.down()

# giving color to turtle's pen
t.color("white")

# start filling the color
t.begin_fill()

# making our moon
t.circle(80)

# stop filling the color
t.end_fill()

# after drawing hiding the turtle from
# the window
t.hideturtle()

# terminated the window after clicking
w.exitonclick()
