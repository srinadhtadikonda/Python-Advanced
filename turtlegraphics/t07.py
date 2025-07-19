# import for turtle module
import turtle

# making a workScreen
ws = turtle.Screen()

# defining a turtle instance
geekyTurtle = turtle.Turtle()

# iterating the loop 8 times
for i in range(8):
  
    # moving turtle 100 units forward
    geekyTurtle.forward(100)
    
    # turning turtle 45 degrees so 
    # as to make perfect angle for an octagon
    geekyTurtle.left(45)
