# Patryk Kostek
# Lab 2 Problem 1
#
'''
Algorithm:
drawTriangle
    repeat 3 times
        go forward 100 steps
        turn left 120
    end repeat
end

drawDesign
    repeat 6 times
        drawTriangle
        turn left 60 degrees
    end repeat
end
'''
# setup and configuration of potato, our turtle
import turtle


#  drawing triangle algorithm
def drawTriangle(t, size):
    """ a function that draws a triangle """
    for i in range(3):
        t.forward(size)
        t.left(120)


def drawDesign():
    """ a function that draws the intended design """
    for i in range(6):
        drawTriangle(potato, 100)
        potato.left(60)


wn = turtle.Screen()             #   enable the canvas for our potato
wn.bgcolor("dark magenta")       #   set the canvas to dark magenta
wn.setup(500, 500)

potato = turtle.Turtle()         #   name of our turtle
potato.color("white")            #   set potatos pen color
potato.pensize(6)                #   set potatos width


drawDesign()
wn.exitonclick()

#   the syntax of the turtle commands gave me the most issues here
#   after reading and practicing the syntax, I was able to finish the code