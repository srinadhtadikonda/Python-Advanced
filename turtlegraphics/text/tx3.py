import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()
t.penup()

colors = ["red", "blue", "green", "purple", "orange"]
index = 0

def animate():
    global index

    t.clear()
    t.color(colors[index])
    t.write("Hello, Turtle!",
            align="center",
            font=("Arial", 30, "bold"))

    index = (index + 1) % len(colors)

    screen.ontimer(animate, 300)

animate()
turtle.done()
