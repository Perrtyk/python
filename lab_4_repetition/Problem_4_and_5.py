"""
    Problem_4
    Edit your Rock Paper Scissors game from lab 3 to validate the user's input.
    When the user enters something other than Rock, Paper or Scissors he/she/they
    should be forced reenter a choice.  Your solution should add a "fruitful"
    function named getUserChoice that takes no parameters and returns a string.
    In the body of the function, a while loop should be used to force the user to
    reenter a choice until the input is valid.  main will call the function
    getUserChoice rather than calling the function input to get the user's input
    but otherwise should remain unchanged.

Adjustments:
    make gather_input fruitful with while loop
Algorithm:
    Import Rock paper scissors game, change to main(4)

    gather input():
    while true
        rest of function

    Problem_5
    Edit your Rock Paper Scissors game from number 4 above to allow the user to
    play again.  Your solution should add a "fruitful" function named getPlayAgain
    that takes no parameters and returns either True or False.  Your solution will
    include this one new function and main will include a loop.

Adjustments:
    create get_playagain function and incorporate in main, put loop in main
Algorithm:
    get_playagain():
        while true
            assign playagain to input from user
                if playagain.lower() is yes
                    then return true
                elif playagain.lower() is no
                    then return false
                else
                    print error message for error handling

"""

#   import random library for randint function use
import random
#   constant list
ROCK, PAPER, SCISSORS = 1, 2, 3
CHOICES = {1: 'rock', 2: 'paper', 3: 'scissors'}


def welcome():
    print(f'Welcome to Rock, Paper, Scissors game.\n'
          f'Which would you like to choose? \033[1m(Rock, Paper, Scissors)\033[0m')


#   gathers input from users and returns 1, 2, or 3 based on input
def gather_input():
    """ gathers input from user and defines u_choice """
    while True:
        u_choice = input('Selection: ')
        if u_choice.lower() == 'rock':
            return ROCK
        elif u_choice.lower() == 'paper':
            return PAPER
        elif u_choice.lower() == 'scissors':
            return SCISSORS
        else:
            print(f'\033[91mValidation Error\033[0m: Value not rock, paper or scissors.'
                  f' Please try again.')


#   defines winning combination for if statement, uses choices to determine winner
def display_winner(u_choice, c_choice):
    """ displays winner in message based in u_choice and c_choice """
    WINNING_COMBINATIONS = [(ROCK, SCISSORS), (SCISSORS, PAPER), (PAPER, ROCK)]
    if u_choice == c_choice:
        message = f"It's a Tie! The computer chose {CHOICES[c_choice]}."
    elif (u_choice, c_choice) in WINNING_COMBINATIONS:
        message = f'You \033[92mwin\033[0m, {CHOICES[u_choice]} beats {CHOICES[c_choice]}!'
    else:
        message = f"Sorry, you \033[91mlose\033[0m!\nYou chose {CHOICES[u_choice]}"\
                  f" and the computer chose {CHOICES[c_choice]}."
    return message


def get_playagain():
    while True:
        user_input = input('Would you like to play again?: ')
        if user_input.lower() == 'yes':
            return True
        elif user_input.lower() == 'no':
            return False
        else:
            print(f'\033[91mValidation Error\033[0m: Value not yes or no.'
                  f' Please try again.')


#   runs the main body of the code
def main4():
    """ prints welcome statement, instructions, and runs code for problem 4 """
    welcome()
    u_choice = gather_input()
    c_choice = random.randint(1, 3)
    if u_choice in CHOICES:
        message = display_winner(u_choice, c_choice)
        print(message)
    else:
        print('Please select an option from the selection.')
    return


def main5():
    """ prints welcome statement, instructions, and runs code for problem 5 """
    welcome()
    while True:
        u_choice = gather_input()
        c_choice = random.randint(1, 3)
        message = display_winner(u_choice, c_choice)
        print(message)
        playagain = get_playagain()
        if playagain is False:
            break

#   call main when this file is run
if __name__ == '__main__':
    main5()
