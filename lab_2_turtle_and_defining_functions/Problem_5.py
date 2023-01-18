# Patryk Kostek
# Lab 2 Problem 5
#
"""
Algorithm:
draw_side
    repeat 3 times
        move forward 25 steps
        turn left 90 degrees
        move forward 25 steps
        turn right 90 degrees
    end repeat
    move forward 25 steps
end

draw_design
    repeat 4 times
        draw_side
        turn left 90
    end repeat
    turn left 90
end
"""

import turtle


#   this section is for configuring the screen of the turtle
def init_screen():
    """ Initialize the turtle screen """
    WIDTH, HEIGHT = 500, 500
    screen = turtle.Screen()
    screen.bgcolor('white')
    screen.setup(WIDTH, HEIGHT)
    screen.title("Lab 2 Problem 5")
    return screen


#   this section is for configuring the turtle
def init_potato(t):
    """ Initialize the turtle (t - turtle) """
    t.speed(3)
    t.color("Grey")
    t.pensize(2)
    t.penup()
    t.goto(-25, -100)
    t.pendown()
    return t


#   function to draw the first side of the shape
def draw_side(t):
    """ Draws sides using the t turtle """
    for i in range(3):
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(90)
    t.forward(25)
    return t


#   function to draw the complete shape using the draw_side(t) function
def draw_design(t):
    """ Draws the design using the draw_side function """
    for i in range(4):
        draw_side(t)
        t.left(90)
    t.left(90)
    return t


#   this is the main function that runs the final code
def main():
    """ Runs the main function of the code """
    potato = init_potato(turtle.Turtle())
    screen = init_screen()
    draw_design(potato)
    screen.exitonclick()


main()

#   With this problem I tried my best to finish the code with one defined function as well
#   as make the code easily readable and adjustable. the goal for me was to allow users to
#   adjust the turtle and screen variables easily. I also tried my best to provide as little
#   'weak warnings' from pyCharm as possible. There are currently 2 left in this code being
#   capital variable HEIGHT and WIDTH.
