# Patryk Kostek
# Lab 2 Problem 3
#
'''
Algorithm:
drawCross
    repeat 1 times
        move forward 75 steps
        drawPlus
    end repeat
end

drawPlus
    repeat 3 times
        turn right 90
        go forward 25 steps
        turn left 180
        go forward 25 steps
    end repeat
end

drawDesign
    repeat 4 times
        drawCross
        turn right 90
        go forward 75
'''

import turtle

WIDTH, HEIGHT = 500, 500

#   Configuration for the GUI screen of the program


def initScreen():
    """ Initializes the screen called screen """
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.setup(WIDTH, HEIGHT)
    wn.title("Lab 2 Problem 3")
    return wn

#   Building screen variable into the main body of the code to use later
wn = initScreen()


def initPotato():
    """ Initializes the turtle called potato """
    potato = turtle.Turtle()         #   name of our turtle
    potato.color("black")            #   set potatos pen color
    potato.pensize(3)                #   set potatos width
    return potato

#   Building the potato variable into the main body of the code to use for later
potato = initPotato()


def drawCross():
    """Draws the cross """
    for i in range(1):
        potato.forward(75)
        drawPlus()


def drawPlus():
    """ Draws the plus of the cross """
    for i in range(3):
        potato.right(90)
        potato.forward(25)
        potato.right(180)
        potato.forward(25)


def drawDesign():
    """ Draws the design of 4 crosses interlaced """
    for i in range(4):
        drawCross()
        potato.right(90)
        potato.forward(75)
        potato.right(90)
    potato.left(90)


drawDesign()
wn.exitonclick()

#   This problem, I was attempting to put as much of the code into defined functions as possible
#   I researched that this is best practice as it allows you to adjust the code in one
#   location and alter it in many places within the code. Currently, I am unsure if I have done
#   it correctly but I am proud of the outcome.