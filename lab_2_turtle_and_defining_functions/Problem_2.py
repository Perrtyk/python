# Patryk Kostek
# Lab 2 Problem 2
#
'''
Algorithm:
drawSquare
    repeat 4 times
        go forward 100 steps
        turn left 90
    end repeat
end

drawRow
    repeat 3 times
        draw square
        move forward 100 steps
    end repeat
end

returnPosition
    repeat 1 times
        move right 90 degrees
        move forward 300 steps
        move right or left 180 degrees

drawDesign
    repeat 6 times
        drawTriangle
    end repeat
    returnPosition
end
'''

import turtle

#   potato configuration for turtle

wn = turtle.Screen()
wn.bgcolor("white")

potato = turtle.Turtle()         #   name of our turtle
potato.color("black")            #   set potatos pen color
potato.pensize(3)                #   set potatos width

def drawSquare():
    """ defined function to draw a square """
    for drawSquare in range(4):
        potato.forward(100)
        potato.left(90)

def drawRow():
    """ defined function to draw a row of squares """
    for drawRow in range(3):
        drawSquare()
        potato.forward(100)

def drawDesign():
    """ defined function to draw the final design of a 3x3 square"""
    for drawDesign in range(3):
        drawRow()
        potato.left(180)
        potato.forward(300)
        potato.right(90)
        potato.forward(100)
        potato.right(90)
    returnPosition()

def returnPosition():
    """ returns position of potato to required 0,0 """
    potato.home()
    potato.left(90)

drawDesign()
wn.exitonclick()

#   the issue I encountered here was mainly the turning degree radius of the turtle
#   there were a couple of times I encountered issues of potato making interesting shapes
#   originally I returned the position by telling potato where to go via steps and degrees
#   I found the variable.home() command and used it to clean up the code