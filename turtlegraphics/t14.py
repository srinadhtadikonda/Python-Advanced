#Rainbow
# Import turtle package
import turtle

# Creating a turtle screen object
sc = turtle.Screen()

# Creating a turtle object (pen)
pen = turtle.Turtle()

# Defining a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col, rad, val):

    # Set the fill/drawing color of the semicircle
    pen.color(col)

    # Draw a semicircle
    pen.circle(rad, -180)

    # Move the turtle up
    pen.up()

    # Move the turtle to a given position
    pen.setpos(val, 0)

    # Move the turtle down
    pen.down()

    # Turn the turtle around
    pen.right(180)


# Set the colors for drawing
col = [
    'violet',
    'indigo',
    'blue',
    'green',
    'yellow',
    'orange',
    'red'
]

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('black')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
    semi_circle(
        col[i],
        10 * (i + 8),
        -10 * (i + 1)
    )

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
