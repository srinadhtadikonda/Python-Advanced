import turtle
from math import cos,sin, pi

window = turtle.Screen()
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
myPen.pensize(2)
myPen.color("red")

R = 125
r = 85
d = 125
angle = 0

myPen.up()
myPen.goto(R-r+d,0)
myPen.down()

theta = 0.2
steps = 8 * int(6*pi/theta)

for t in range(0,steps):
    angle+=theta
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    myPen.goto(x,y)

myPen.done()
