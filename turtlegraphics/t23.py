# import turtle package
import turtle


# function for movement of an object 
def moving_object(move):
    
    # to fill the color in ball
    move.fillcolor('orange') 
    
    # start color filling
    move.begin_fill() 
    
    # draw circle
    move.circle(20)  
    
    # end color filling
    move.end_fill()             

# Driver Code
if __name__ == "__main__" :
    
    # create a screen object
    screen = turtle.Screen() 

    # set screen size
    screen.setup(600,600)    

    # screen background color
    screen.bgcolor('green')   

    # screen updaion 
    screen.tracer(0)           

    # create a turtle object object
    move = turtle.Turtle() 

    # set a turtle object color
    move.color('orange')

    # set turtle object speed
    move.speed(0) 

    # set turtle object width
    move.width(2)     

    # hide turtle object
    move.hideturtle()          

    # turtle object in air
    move.penup()               

    # set initial position
    move.goto(-250, 0) 

    # move turtle object to surface
    move.pendown()             

    # infinite loop
    while True :
        
        # clear turtle work
        move.clear()  
        
        # call function to draw ball
        moving_object(move)   
        
        # update screen
        screen.update()    
        
        # forward motion by turtle object
        move.forward(0.5)
