# Patryk Kostek
# Lab 4 Problem 6
#
"""

    Design and implement a program that allows the user to play a
    "Guess My Number" game with the computer.  When the game starts
    the program will generate a random number between 1 and 50.  The
    user should be prompted to guess the number and to enter a number
    from the keyboard.  The program will display one of the following
    messages when the user's guess is incorrect:  "Too high" or "Too low".
    The user should be allowed to continue guessing until he/she/they
    guess correctly.  The program should keep track of number of
    guesses that the user makes and should display the number of guesses
    along with a congratulatory message at the end of the game.  Your solution
    must include a function getGuess that gets and validates the number entered
    by the user as well as a main function.  getGuess should take no parameters
    and return a number between 1 and 50 (it is NOT necessary to verify that the
    number is an integer).  main will call getGuess as part of the game loop.

Algorithm:
import random
welcome():
    print welcome message with instructions
    print formatted instructions

get_guess():
    CHOICES = range(1, 51)
    While true:
        try
            get the user_input between 1 and 50
            if user_input in CHOICES
                return user_input
            else
                print invalid message
        except value error
            print error message

main()
    print welcome and instructions
    generate computer input between 1 and 51
    gather user input with get_guess
    while user_input =! computer_input

"""
import random


#   displays the welcome message formatted to be in the center of the screen
def welcome():
    """ displays the initial welcome message """
    width = 100
    string1 = 'Welcome to the guess against the computer game... here is how to play:'
    string2 = 'Select a number from 1 to 50, the computer will tell you whether you are close!\n'
    print(f'{string1:^{width}}')
    print(f'{string2:^{width}}')


#   this gathers the input and validates if within 1-50 range, provides error handling
def get_guess():
    """ gathers the user's guess with error handling, returns the input from 1-50 """
    CHOICES = range(1, 51)
    while True:
        try:
            user_input = int(input('What is your guess?: '))
            if user_input in CHOICES:
                return user_input
            else:
                print(f'\033[91mInvalid Value Error\033[0m: '
                      f'Please choose a number between 1 and 50.')
        except ValueError:
            print(f'\033[91mInvalid Value Error\033[0m: '
                  f'Please choose a number between 1 and 50.')


#   initialize guess and computer_input and run main body of code
def main():
    """ runs Lab 4 Problem 6 """
    welcome()
    guess = 0
    computer_input = random.randint(1, 51)
    while True:
        user_input = get_guess()
        guess += 1
        if user_input != computer_input:
            if user_input > computer_input:
                print('You are too high! , try again...')
            else:
                print('You are too low! , try again...')
        else:
            print('Congratulations! You guessed the correct number!\n'
                  'It took you ' + str(guess) + ' attempts.')
            return False


#   call main when this file is run
if __name__ == '__main__':
    main()

#   This problem was very fun and great for learning while loops. I enjoyed adding the extra
#   complexity of keeping the attempts score. This was very fun to code. Some issues I
#   encountered were still with the formatting of text. Formatting text seems to be the
#   topic always giving me issues.
