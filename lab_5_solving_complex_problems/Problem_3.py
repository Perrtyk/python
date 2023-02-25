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


def welcome():
    WIDTH1, WIDTH2 = (71), (79)
    start_bold, end_bold = ('\033[1m', '\033[0m')
    string_welcome = f'{start_bold}Welcome to Nim!{end_bold}'
    string_instruct1 = 'Players will take turns removing 1, 2, or 3 sticks from the initial 11.'
    string_instruct2 = 'The player removing the last stick wins!\n'
    print(f'{string_welcome:^{WIDTH2}}\n\n'
          f'{string_instruct1}\n'
          f'{string_instruct2:^{WIDTH1}}')


def game_state(score_value):
    """ Based on score, returns the game mark and score """
    WIDTH1 = (43)
    start_bold, end_bold = ('\033[1m', '\033[0m')
    mark = f' | '
    string_score = f'{start_bold}Game Status:{end_bold}' \
                   f'{mark * score_value:^{WIDTH1}}\n'
    return string_score


def game_input():
    ERROR = '\033[91mERROR\033[0m:'
    CHOICES = [1, 2, 3]
    while True:
        try:
            user_input = int(input('How many sticks would you like to remove? (1, 2, or 3?): '))
            print()
            if user_input not in CHOICES:
                print(ERROR)
            else:
                break
        except ValueError:
            print('Value' + ERROR)
    return user_input


def game_process(user_choice, comp_choice, current_score):

    new_score = (current_score - user_choice)
    if new_score == 0:
        winner = 'user'
        print(f'Your choice is \033[92m{user_choice}\033[0m.')
        return new_score, winner
    else:
        print(f'Your choice is \033[92m{user_choice}\033[0m.')
        time.sleep(0.5)
        print(game_state(new_score))
        time.sleep(0.5)

    new_score -= comp_choice
    if new_score == 0:
        winner = 'computer'
        print(f'The computers choice is \033[91m{comp_choice}\033[0m.')
        return new_score, winner
    else:
        winner = 'none'
        print(f'The computers choice is \033[91m{comp_choice}\033[0m.')
        time.sleep(0.5)
        print(game_state(new_score))
        time.sleep(0.5)
    return new_score, winner






def main3():
    welcome()
    score = 11
    winner = ()
    print(game_state(score))

    # loop
    while True:
        try:
            user_choice = game_input()
            new_score = (score - user_choice)
            if user_choice > score:
                print(f"You cannot remove that many sticks. Try between 1 and {score}.")
                continue
            if new_score > 3:
                computer_choice = random.randint(1, 3)
            else:
                computer_choice = random.randint(1, new_score)

            score, winner = game_process(user_choice, computer_choice, score)
            if score == 0:
                break
        except ValueError:
            print('Value error')
    print(f'The winner is {winner}')

if __name__ == '__main__':
    main3()

"""

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

"""

