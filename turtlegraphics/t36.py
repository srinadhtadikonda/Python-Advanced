# click_rose.py
from turtle import *
from random import *

tracer(1000, 0)

def draw_rose(x, y):
    # Set pen color and size for roses:
    pencolor('red')
    pensize(randint(2, 5))

    # Move to the XY coordinates of the mouse click:
    penup()
    goto(x, y)
    pendown()

    # Draw a rose:
    for i in range(100):
        pencolor((random(), 0, 0))
        pensize(randint(2, 5))
        forward(i)
        left(randint(50, 70))
    update()


bgcolor('black')

# Set the draw_rose() function to be called when a click happens:
getscreen().onclick(draw_rose)

done()
