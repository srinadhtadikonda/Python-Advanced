import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.penup()

def write_text(x, y):
    t.goto(x, y)
    t.write("Clicked!", align="center", font=("Arial", 14, "bold"))

screen.onclick(write_text)

turtle.done()
