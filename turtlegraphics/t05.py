
from turtle import *

title("Circle Drawing")
setup(500, 500)
bgcolor("black")
shape("turtle")   
pencolor("blue")     # Line color
fillcolor("cyan")    # Fill color for the shape     # Pen color
pensize(5)
speed(1)

# Begin drawing
begin_fill()
circle(100, 360)
end_fill()

done()
