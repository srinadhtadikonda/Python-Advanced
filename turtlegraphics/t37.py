# curve_path.py

from turtle import *
from random import *

tracer(4, 0)

for i in range(100):  # Draw 100 curvy paths.
    # Move the turtle back to 0, 0:
    penup()
    home()
    pendown()

    # Set a random heading and draw several short lines with changing direction:
    setheading(randint(0, 360))
    for j in range(randint(200, 600)):  # Each curve has 200 to 600 segments.
        forward(1)  # Each segment is 1 step long.
        left(randint(-4, 4))  # Change the direction slightly


update()
done()
