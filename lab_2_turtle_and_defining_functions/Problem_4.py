# Patryk Kostek
# Lab 2 Problem 4
#
'''
Algorithm:
drawZig
    repeat 2 times
        move forward 200 steps
        turn left 90 degrees
        move forward 50 steps
        turn left 90 degrees
        move forward 200 steps
        turn right 90 degrees
        move forward 50 steps
        turn right 90 degrees
    end repeat
end

drawDesign
    drawZig
    move forward 200 steps
end
'''

import turtle


#   this section is for configuring the screen of the turtle
def initScreen():
    ''' Initialize the turtle screen '''
    WIDTH, HEIGHT = 500, 500
    screen = turtle.Screen()
    screen.bgcolor('white')
    screen.setup(WIDTH, HEIGHT)
    screen.title("Lab 2 Problem 4")
    return screen


#   this section is for configuring the turtle
def initPotato(t):
    ''' Initialize the turtle (t - turtle) '''
    t.color("Black")
    t.pensize(1)
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    return t


#   this function draws the initial zig pattern
def drawZig(t):
    ''' Draw the Zig shape (t - turtle) '''
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.right(90)
    return t


#   this function draws the design required
def drawDesign(t):
    ''' Draw the final design (t - turtle) '''
    drawZig(t)
    t.forward(200)
    t.penup()
    t.forward(500)
    return t


#   this function calls the main code of the program
def main():
    ''' Runs the main function with parameter of how many times '''
    screen = initScreen()
    potato = initPotato(turtle.Turtle())
    drawDesign(potato)
    screen.exitonclick()
    return main


main()

#   this problem I began to experiment with putting all my code into defined functions
#   it ended well but I struggled a lot with parameters. I tried to use them more to get
#   practice

