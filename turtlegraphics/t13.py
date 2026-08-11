import turtle

scr = turtle.Screen()
clr = ['red', 'green', 'blue', 'yellow', 'purple']

turtle.pensize(4)
turtle.penup()
turtle.setpos(-90, 30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(clr[i])
    turtle.forward(200)
    turtle.right(144)

turtle.penup()
turtle.setpos(80, -140)
turtle.pendown()
turtle.pencolor("black")

turtle.done()
