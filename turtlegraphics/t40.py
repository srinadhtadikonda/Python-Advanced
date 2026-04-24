# importing package
import turtle

# function to draw
# colored star
def colored_star():
    
    # size of star
    size = 80
    
    # object color
    turtle.color("red")
    
    # object width
    turtle.width(4)
    
    # angle to form star
    angle = 120
    
    # color to fill
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    
    # form star
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
        
    # fill color
    turtle.end_fill()

# Driver code
colored_star()
