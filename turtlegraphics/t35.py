# turtle_directions.py
from turtle import *

for i in range(24):
    forward(100)  # Move forward in the current direction.
    write(heading(), font=('Arial', 20, 'normal'))  # Write the degrees of the direction.
    backward(100)  # Move back to the center.
    left(15)  # Turn left by 15 degrees and repeat.
done()
When you run this program, 
