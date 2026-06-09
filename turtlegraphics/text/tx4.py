import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create turtles for each text line
messages = [
    "Hello, Turtle!",
    "Python Animation",
    "Moving Text",
    "Color Effects",
    "Fun with Graphics"
]

colors = [
    "red", "orange", "yellow",
    "green", "cyan", "blue",
    "purple", "pink", "white"
]

texts = []

for msg in messages:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    texts.append({
        "turtle": t,
        "text": msg,
        "x": random.randint(-300, 300),
        "y": random.randint(-200, 200),
        "dx": random.choice([-3, -2, 2, 3]),
        "dy": random.choice([-3, -2, 2, 3]),
        "size": random.randint(16, 30)
    })

def animate():
    for item in texts:
        t = item["turtle"]

        # Erase previous text
        t.clear()

        # Update position
        item["x"] += item["dx"]
        item["y"] += item["dy"]

        # Bounce off walls
        if item["x"] > 350 or item["x"] < -350:
            item["dx"] *= -1

        if item["y"] > 250 or item["y"] < -250:
            item["dy"] *= -1

        # Move and draw
        t.goto(item["x"], item["y"])
        t.color(random.choice(colors))

        t.write(
            item["text"],
            align="center",
            font=("Arial", item["size"], "bold")
        )

    screen.ontimer(animate, 50)

animate()
turtle.done()
