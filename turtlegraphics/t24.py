import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('Green')

# tell screen to not 
# show automatically
screen.tracer(0)            

t = turtle.Turtle()
t.speed(0)
t.width(3)

# hide donatello, we
# only want to see the drawing
t.hideturtle()            

def draw_square() :
    t.fillcolor("Orange")
    t.begin_fill()
    for side in range(4) :
        t.forward(100)
        t.left(90)
    t.end_fill()
t.penup()
t.goto(-350, 0)
t.pendown()

while True :
    t.clear()
    draw_square()
    
    # only now show the screen,
    # as one of the frames
    screen.update()         
    t.forward(0.02)
    
# This code is contributed by pulkitagarwal03pulkit
