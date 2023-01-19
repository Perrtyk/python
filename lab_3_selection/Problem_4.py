#
# Patryk Kostek
# Lab 3 Problem 4
#
'''
    Design and implement a program that asks the user to enter two of 3 primary colors,
    red, yellow or blue.  The program should display a message indicating the secondary
    color that is produced by mixing the two primary colors chosen.  Red + Yellow is
    Orange, Red + Blue is Purple, Yellow + Blue is Green.  It is NOT necessary to
    validate the input from the user.  Your solution should have a function called
    displayColor as well as a main function.  displayColor should have 2 parameters,
    the first and second color.  It should display the secondary color based on the 2
    parameter colors.  main should get the input from the user and call the displayColor
    function.


IPO Chart:
    Input
        color1, color2
    Processing
        display welcome message
        gather color1, color2 inputs from user
        display_color function to gather color3
        display message with color3
    Output
        display message with color3


Algorithm:
    gather_input
        gather input, define color1
        gather input, define color2
        return color1 and color2
    end gather_input

    display_color(color1, color2)
            if color1 is red and color2 is yellow
                then color3 is orange
            elsif color1 is red and color2 is blue
                then color3 is purple
            elsif color1 is yellow and color2 is blue
                then color3 is green
            else
                state error handle code
     end display_color
        
    main
        define the list of combination colors
        print the welcome message
        define color1 and color2 from gather_input
        define color 3 from display_color
        if color 3 is in list of combination colors
            print the color mixture
        else print the error handling message
    end main
'''


def gather_input():
    """ gathers the input from user for color1 and color2 """
    color1 = input('Color 1: ')
    color2 = input('Color 2: ')
    return color1, color2


def display_color(color1, color2):
    """ checks for color combinations of color1 and color2 against lists """
#   defines color3 for later use / error handling
    color3 = None
#   defining the color lists
    orange, purple, green = ['red', 'yellow'], ['red', 'blue'], ['yellow', 'blue']
#   check if color1 and color2 in orange combination list, set color3 to orange
    if color1.lower() in orange and color2.lower() in orange:
        color3 = "\033[33m orange \033[0m"
#   check if color1 and color2 in purple combination list, set color3 to purple
    elif color1.lower() in purple and color2.lower() in purple:
        color3 = "\033[35m purple \033[0m"
#   check if color1 and color2 in green combination list, set color3 to green
    elif color1.lower() in green and color2.lower() in green:
        color3 = "\033[32m green \033[0m"
#   prints error message if invalid color is provided
    else:
        print(f'Error: {color1} or {color2} are an invalid combination from above.\n'
              f'try this...  Color1: yellow')
#   returns the mixed color as variable color3 for use in main() function
    return color3


def main():
    """ prints welcome message and provides the main program """
    combo_color = ['\033[33m orange \033[0m',
                   '\033[35m purple \033[0m',
                   '\033[32m green \033[0m']
    print("Welcome to the color mixer! Please select 2 of these colors!\n"
          "     Yellow     Red     Blue     ")
    color1, color2, = gather_input()
    color3 = display_color(color1, color2)
    if color3 in combo_color:
        print(f'Your colors mixed into{color3}!')
    else:
        print('Error: These values cannot be mixed.')


#   call main when this file is run
if __name__ == '__main__':
    main()

#   With this program, I had fun experimenting with lists for the first time. Using lists
#   I was able to cut down on the amount of code significantly. I also began to learn how
#   to adjust the font color of the string commands.