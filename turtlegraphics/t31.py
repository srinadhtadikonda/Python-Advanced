from turtle import *
import math

screen = Screen()
screen.setup(1000,1000)
screen.title("Hypotrochoid with Python Turtle")
screen.tracer(0,0)

speed(0)
hideturtle()
up()
pensize(2)
t = Turtle()
t.up()
t.hideturtle()
t.speed(0)
tt = Turtle()
tt.hideturtle()
tt.speed(0)
first = True

r_big=300
r_small=r_big/2.1
d = r_big/1.6

t3 = Turtle()
t3.hideturtle()
t3.speed(0)
t3.pensize(2)
t3.up()
t3.seth(0)
t3.goto(0,-r_big)
t3.down()
#t3.circle(r_big,steps=200)

tt.up()
tt.pensize(1)
tt.color('red')
first = True

def draw_circle(x,y,angle):
    global first
##    clear()
##    up()
##    seth(0)
##    goto(x,y-r_small)
##    down()
##    color('black')
#    circle(r_small,steps=200)
    up()
    goto(x,y)
    dot(10,'blue')
    down()
    seth(angle)
    color('purple')
    fd(d)
    dot(10,'red')
    tt.goto(xcor(),ycor())
    if first:
        tt.down()
        first = False

angle = 0
dist = -r_small*angle*math.pi/180
big_radian = dist/r_big
x = (r_big-r_small)*math.cos(big_radian)
y = (r_big-r_small)*math.sin(big_radian)
draw_circle(x,y,angle+big_radian*180/math.pi)
while True:
    angle -= 6
    dist = -r_small*angle*math.pi/180
    big_radian = dist/r_big
    x = (r_big-r_small)*math.cos(big_radian)
    y = (r_big-r_small)*math.sin(big_radian)
    draw_circle(x,y,angle+big_radian*180/math.pi)
    if angle % 360 == 0 and int(round(big_radian*180/math.pi)) % 360 == 0:
        break
    update()

# uncomment to get only the last curve
#clear()
t3.clear()
update()

done()
