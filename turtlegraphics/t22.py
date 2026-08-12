#star sky
import turtle
import random

# ==========================================
# CREATE SCREEN
# ==========================================

screen = turtle.Screen()
screen.setup(1200, 700)
screen.bgcolor("black")
screen.title("⭐ Starry Sky 🌙")


# ==========================================
# CREATE TURTLE
# ==========================================

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# ==========================================
# FUNCTION TO DRAW A STAR
# ==========================================

def draw_star(x, y, size):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color("white")
    t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()


# ==========================================
# DRAW RANDOM STARS
# ==========================================

for i in range(100):

    x = random.randint(-550, 550)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)

    draw_star(x, y, size)


# ==========================================
# DRAW MOON
# ==========================================

t.penup()
t.goto(-80, 150)
t.pendown()

t.color("white")
t.begin_fill()

t.circle(80)

t.end_fill()


# ==========================================
# CREATE MOON SHADOW
# ==========================================

t.penup()
t.goto(-45, 175)
t.pendown()

t.color("black")
t.begin_fill()

t.circle(80)

t.end_fill()


# ==========================================
# ADD LARGER YELLOW STARS
# ==========================================

for i in range(10):

    x = random.randint(-550, 550)
    y = random.randint(-300, 300)

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color("yellow")

    for j in range(5):
        t.forward(12)
        t.right(144)


# ==========================================
# HIDE TURTLE
# ==========================================

t.hideturtle()


# ==========================================
# KEEP WINDOW OPEN
# ==========================================

screen.exitonclick()
