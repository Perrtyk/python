"""
Patryk Kostek
Lab 5 Problem 3

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
    return f'\033[91m{text}\033[0m'


def font_green(text):
    """ Returns text in red color. """
    # used for making text green without clutter
    return f'\033[92m{text}\033[0m'


def welcome():
    """ Prints initial welcome message with instructions. """
    # set 2 widths for centering the strings
    WIDTH1, WIDTH2 = (71, 79)
    print()
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
    string_score2 = bold((f'Sticks Remaining: '))
    print(f'{string_score2}{score_value}')
    return string_score


def game_input(current_score):
    """ Gathers the user's input with error handling built in. """
    # defining of error messages
    ERROR01, ERROR02 =  bold(font_red('ERROR 01:')) + ' Choice error, please select a number from 1 to 3.', \
                        bold(font_red('ERROR 02:')) + ' Value error, please select a valid number.'
    # defining our choice list the user will be able to choose from
    CHOICES = [1, 2, 3]
    # while loop gathering the users input with error handling
    while True:
        try:
            user_input = int(input('How many sticks would you like to remove? '
                                   + bold('(1, 2, or 3?): ')))
            print()
            if user_input not in CHOICES:
                print(ERROR01)
            elif user_input > current_score:
                print(f"You cannot remove that many sticks. Try between 1 and {current_score}.\n")
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
    """ Main game process computing the new score and winner. """
    new_score = (current_score - user_choice)
    if new_score == 0:
        winner = 'user'
        print(f'Your choice is ' + font_green(user_choice) + '.\n')
        return new_score, winner
    else:
        print(f'Your choice is ' + font_green(user_choice) + '.\n')
        time.sleep(0.5)
        print(game_state(new_score))
        time.sleep(0.5)

    new_score -= comp_choice
    if new_score == 0:
        winner = 'computer'
        print(f'The computer choice is ' + font_red(comp_choice) + '.\n')
        return new_score, winner
    else:
        winner = ''
        print(f'The computer choice is ' + font_red(comp_choice) + '.\n')
        time.sleep(0.5)
        print(game_state(new_score))
        time.sleep(0.5)
    return new_score, winner


def play_again():
    """ Asks the user if they would like to play again. """
    string1 = 'Would you like to play again? ' + font_green(bold('(yes/no): '))
    play_choice = input(string1)
    if play_choice.lower() == 'yes':
        return True
    else:
        return exit()


def main3():
    """ Main function running the game. """
    # establishment of True for play_choice so that we could play the game
    play_choice = True
    # start of play again loop
    while play_choice == True:
        # prints the welcome message
        welcome()
        # sets the initial score to 11
        score = 11
        # prints the score statement
        print(game_state(score))
        # starts the game cycle
        while True:
            user_choice = game_input(score)
            new_score = (score - user_choice)
            computer_choice = comp_input(new_score)
            score, winner = game_process(user_choice, computer_choice, score)
            if score == 0:
                break
        if winner == 'user':
            print('You ' + bold(font_green('won')) + '!\n')
        else:
            print('You ' + bold(font_red('lost')) + '!\n')
        print(f'The winner is the ' + bold(winner) + '!\n')
        # prompts the user if they want to play again
        play_choice = play_again()


if __name__ == '__main__':
    main3()

'''
This problem was more difficult than others but very fun to do. The difficult parts were the
amount of loops and functions within the program and keeping track of variables and parameters
began to become challenging. Many times, my loops were broken and it took a lot of debugging
to get this program to behave.
'''
