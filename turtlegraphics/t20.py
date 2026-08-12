#clock
import turtle
import datetime
import time

# -----------------------------
# Create Screen
# -----------------------------
screen = turtle.Screen()
screen.title("Digital Clock")
screen.bgcolor("black")
screen.setup(width=600, height=300)

# -----------------------------
# Create Border Turtle
# -----------------------------
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.color("cyan")

border.penup()
border.goto(-250, 80)
border.pendown()

for i in range(2):
    border.forward(500)
    border.right(90)
    border.forward(120)
    border.right(90)

# -----------------------------
# Create Clock Turtle
# -----------------------------
clock = turtle.Turtle()
clock.hideturtle()
clock.penup()
clock.goto(0, 15)

# -----------------------------
# Create Date Turtle
# -----------------------------
date_display = turtle.Turtle()
date_display.hideturtle()
date_display.penup()
date_display.goto(0, -50)

# -----------------------------
# Create Title Turtle
# -----------------------------
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.goto(0, 110)

title.color("yellow")
title.write(
    "DIGITAL CLOCK",
    align="center",
    font=("Arial", 20, "bold")
)

# -----------------------------
# Update Clock
# -----------------------------
while True:

    # Get current date and time
    now = datetime.datetime.now()

    # Convert to 12-hour format
    hour = now.hour

    if hour == 0:
        hour = 12
        period = "AM"
    elif hour < 12:
        period = "AM"
    elif hour == 12:
        period = "PM"
    else:
        hour = hour - 12
        period = "PM"

    minute = now.minute
    second = now.second

    # Format time
    current_time = (
        str(hour).zfill(2)
        + ":"
        + str(minute).zfill(2)
        + ":"
        + str(second).zfill(2)
    )

    # Format date
    current_date = now.strftime("%d-%m-%Y")

    # Clear old clock
    clock.clear()

    # Display time
    clock.color("lime")
    clock.write(
        current_time,
        align="center",
        font=("Courier New", 40, "bold")
    )

    # Display AM / PM
    clock.goto(180, 15)
    clock.color("orange")
    clock.write(
        period,
        align="center",
        font=("Arial", 18, "bold")
    )

    # Reset position for next update
    clock.goto(0, 15)

    # Clear and display date
    date_display.clear()
    date_display.color("white")
    date_display.write(
        current_date,
        align="center",
        font=("Arial", 18, "bold")
    )

    # Wait one second
    time.sleep(1)

# Keep window open
turtle.done()
