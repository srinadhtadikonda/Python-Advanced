import turtle

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "blue", "green", "orange"]

for i in range(4):
    pen.color(colors[i])
    
    pen.begin_fill()
    
    pen.forward(120)
    pen.left(150)
    pen.forward(120)
    pen.left(30)
    
    pen.end_fill()
    
    pen.right(90)

# Center
pen.color("black")
pen.penup()
pen.goto(-10, -10)
pen.pendown()
pen.begin_fill()
pen.circle(10)
pen.end_fill()

turtle.done()
