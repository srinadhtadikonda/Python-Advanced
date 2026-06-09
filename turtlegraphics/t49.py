import turtle
import colorsys
#screen setup
screen=turtle.Screen()
screen.bgcolor("black")
#turtle setup
t=turtle.Turtle()
t.speed(0)
turtle.delay(0)
#drawing part
h=0
for x in range(200):
    color=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(color)
    h +=0.005
    t.forward(x*2)
    t.right(119)    #canging this angle creates different shapes
turtle.done()
