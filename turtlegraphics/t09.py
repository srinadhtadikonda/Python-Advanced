import turtle

t = turtle.Turtle()

s = int(input("side of the star: "))

col = input("color name or hex value of color(#RRGGBB): ")

t.fillcolor(col)

t.begin_fill()

# drawing the star of side s
for _ in range(5):
    t.forward(s)
    t.right(144)

t.end_fill()
