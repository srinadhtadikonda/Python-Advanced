import turtle

t = turtle.Turtle()

t.penup()          # Don't draw while moving
t.goto(0, 0)       # Position where text will appear
t.write("Hello, Turtle!", align="center", font=("Arial", 16, "normal"))

turtle.done()
