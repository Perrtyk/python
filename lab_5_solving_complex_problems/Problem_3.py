"""

Design and implement a program that allows the user to play a version of Nim against the
computer.  Nim is a mathematical strategy game, which dates to 16th century China.  There
are many variations on this game, but the version we’ll be playing starts with a row of
11 sticks. On their turn a player may remove 1, 2, or 3 sticks from the pile. Players
alternate taking turns, and the play removing the last stick wins.

First, your program should print out a welcome statement and brief instructions. Then, you
should display the current game state and prompt the player for the number of sticks they
want to remove. After making sure they entered a valid response, you should remove the appropriate
number of sticks. If there are now zero sticks remaining, you should declare that player the
winner and end the program. Otherwise, the computer should take a turn. The computer should randomly
choose the number of sticks to remove.  Here's a sample of what your output might look like:

"""
import time
import random


def bold(text):
    """ Returns text in bold. """
    # used for making text bold without clutter
    return f'\033[1m{text}\033[0m'


def font_red(text):
    """ Returns text in red color. """
    # used for making text red without clutter
    return f'\033[91m{text}\033[0m:'


def welcome():
    """ Prints initial welcome message with instructions. """
    # set 2 widths for centering the strings
    WIDTH1, WIDTH2 = (71, 79)
    string_welcome = bold('Welcome to Nim!')
    string_instruct1 = 'Players will take turns removing 1, 2, or 3 sticks from the initial 11.'
    string_instruct2 = 'The player removing the last stick wins!\n'
    print(f'{string_welcome:^{WIDTH2}}\n\n'
          f'{string_instruct1}\n'
          f'{string_instruct2:^{WIDTH1}}')


def game_state(score_value):
    """ Based on the sticks left, returns the game marks and score """
    # set width for centering the string
    WIDTH1 = 43
    mark = f' | '
    string_score = bold('Game Status:') + str(f'{mark * score_value:^{WIDTH1}}\n')
    return string_score


def game_input(current_score):
    """ Gathers the user's input with error handling built in. """
    #
    ERROR01, ERROR02 = font_red('ERROR 01') + ' Choice error, please select a number from 1 to 3.', \
                       font_red('ERROR 02') + ' Value error, please select a valid number.'
    CHOICES = [1, 2, 3]
    while True:
        try:
            user_input = int(input('How many sticks would you like to remove? (1, 2, or 3?): '))
            print()
            if user_input not in CHOICES:
                print(ERROR01)
            elif user_input > current_score:
                print(f"You cannot remove that many sticks. Try between 1 and {current_score}.")
            else:
                return user_input
        except ValueError:
            print(ERROR02)


def comp_input(current_score):
    """ Determines the computers choice depending on sticks left. """
    if current_score == 1:
        computer_choice = 1
    elif current_score == 0:
        computer_choice = 0
    elif current_score > 3:
        computer_choice = random.randint(1, 3)
    else:
        computer_choice = random.randint(1, current_score)
    return computer_choice


def game_process(user_choice, comp_choice, current_score):
    """Main game process computing the new score and winner."""
    new_score = (current_score - user_choice)
    winner = ''

    # Check if user wins
    if new_score == 0:
        winner = 'user'
    print(f'Your choice is \033[92m{user_choice}\033[0m.')
    time.sleep(0.5)
    print(game_state(new_score))
    time.sleep(0.5)

    # Check if computer wins
    new_score -= comp_choice
    if new_score == 0:
        winner = 'computer'
    print(f'The computer\'s choice is \033[91m{comp_choice}\033[0m.')
    time.sleep(0.5)
    print(game_state(new_score))
    time.sleep(0.5)

    return new_score, winner


def main3():
    welcome()
    score = 11
    print(game_state(score))

    # loop
    while True:
        user_choice = game_input(score)
        new_score = (score - user_choice)
        computer_choice = comp_input(new_score)
        score, winner = game_process(user_choice, computer_choice, score)
        if score == 0:
            break
    print(f'The winner is {winner}')


if __name__ == '__main__':
    main3()
