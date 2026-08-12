#snake game
import turtle as t
import random
import time

# ==========================================
# GAME VARIABLES
# ==========================================

delay = 0.1
score = 0
high_score = 0


# ==========================================
# CREATE SCREEN
# ==========================================

sc = t.Screen()
sc.title("🐍 Snake Game")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)


# ==========================================
# SNAKE HEAD
# ==========================================

head = t.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


# ==========================================
# FOOD
# ==========================================

food = t.Turtle()
food.speed(0)
food.shape(random.choice(["square", "triangle", "circle"]))
food.color(random.choice(["red", "green", "yellow"]))
food.penup()
food.goto(0, 100)


# ==========================================
# SCORE DISPLAY
# ==========================================

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

pen.write(
    "Score : 0  High Score : 0",
    align="center",
    font=("Arial", 24, "bold")
)


# ==========================================
# DIRECTION FUNCTIONS
# ==========================================

def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


# ==========================================
# MOVEMENT FUNCTION
# ==========================================

def move():

    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


# ==========================================
# KEY BINDINGS
# ==========================================

sc.listen()

sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")


# ==========================================
# SNAKE BODY SEGMENTS
# ==========================================

segments = []


# ==========================================
# MAIN GAME LOOP
# ==========================================

while True:

    sc.update()

    # --------------------------------------
    # CHECK BOUNDARIES
    # --------------------------------------

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):

        time.sleep(1)

        head.goto(0, 0)
        head.direction = "Stop"

        food.goto(
            random.randint(-270, 270),
            random.randint(-270, 270)
        )

        # Remove body segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()

        pen.write(
            f"Score : {score}  High Score : {high_score}",
            align="center",
            font=("Arial", 24, "bold")
        )


    # --------------------------------------
    # CHECK FOOD COLLISION
    # --------------------------------------

    if head.distance(food) < 20:

        food.goto(
            random.randint(-270, 270),
            random.randint(-270, 270)
        )

        # Create new body segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()

        segments.append(new_segment)

        # Increase speed
        delay -= 0.001

        # Increase score
        score += 10

        # Update high score
        if score > high_score:
            high_score = score

        # Update score display
        pen.clear()

        pen.write(
            f"Score : {score}  High Score : {high_score}",
            align="center",
            font=("Arial", 24, "bold")
        )


    # --------------------------------------
    # MOVE BODY SEGMENTS
    # --------------------------------------

    for i in range(len(segments) - 1, 0, -1):

        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()

        segments[i].goto(x, y)


    # Move first body segment
    if len(segments) > 0:

        x = head.xcor()
        y = head.ycor()

        segments[0].goto(x, y)


    # --------------------------------------
    # MOVE SNAKE HEAD
    # --------------------------------------

    move()


    # --------------------------------------
    # CHECK SELF COLLISION
    # --------------------------------------

    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "Stop"

            food.goto(
                random.randint(-270, 270),
                random.randint(-270, 270)
            )

            # Remove body segments
            for body_part in segments:
                body_part.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()

            pen.write(
                f"Score : {score}  High Score : {high_score}",
                align="center",
                font=("Arial", 24, "bold")
            )


    # --------------------------------------
    # GAME SPEED
    # --------------------------------------

    time.sleep(delay)
