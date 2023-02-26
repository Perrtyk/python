"""

Design and implement a program that allows the user to play a version of the dice game Pig
against the computer.  The object of the game is to be the first to score 100 points.  The
user and the computer take turns rolling a pair of dice following these rules:

On a turn each player rolls 2 dice.  If no 1 appears, the total of the dice is added to the
player's score and the player can choose to roll again or pass the turn to the other player.
When the computer does not roll a 1, decide if the computer wants to roll again by
generating a random number between 1 and 2.  1 causes the computer to roll again.  2 causes
the computer to pass.
If a 1 appears on one of the dice, nothing is added to the player's score and the player's turn is over.
If a 1 appears on both dice, the player's score is reset to 0 and the player's turn is over.

"""
import random
import time

WINNING_SCORE = 100


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
    string1 = 'Welcome to Pig.\nThe first person to reach 100 points win.' \
              'You will take turns following these rules:' \
              '1. You will roll dice'


def draw_dice(roll_1, roll_2):
    WIDTH = 10
    draw_1 = (bold(f'{1:^{WIDTH}}\n') +
                '+-------+\n'
                '|       |\n'
                '|   O   |\n'
                '|       |\n'
                '+-------+\n')

    draw_2 = (bold(f'{2:^{WIDTH}}\n') +
                '+-------+\n'
                '| O     |\n'
                '|       |\n'
                '|     O |\n'
                '+-------+\n')

    draw_3 = (bold(f'{3:^{WIDTH}}\n') +
                '+-------+\n'
                '| O     |\n'
                '|   O   |\n'
                '|     O |\n'
                '+-------+\n')

    draw_4 = (bold(f'{4:^{WIDTH}}\n') +
                '+-------+\n'
                '| O   O |\n'
                '|       |\n'
                '| O   O |\n'
                '+-------+\n')

    draw_5 = (bold(f'{5:^{WIDTH}}\n') +
                '+-------+\n'
                '| O   O |\n'
                '|   O   |\n'
                '| O   O |\n'
                '+-------+\n')

    draw_6 = (bold(f'{6:^{WIDTH}}\n') +
                '+-------+\n'
                '| O   O |\n'
                '| O   O |\n'
                '| O   O |\n'
                '+-------+\n')
    DRAW_LIST = {1: draw_1, 2: draw_2, 3: draw_3, 4: draw_4, 5: draw_5, 6: draw_6}
    dice1, dice2 = (DRAW_LIST[roll_1], DRAW_LIST[roll_2])
    return dice1, dice2


def reroll_user():
    while True:
        try:
            roll_choice = int(input('1 - Roll the dice one more time.\n'
                                    '2 - Pass turn to the computer.\n'))
            if roll_choice == 1:
                return True
            elif roll_choice == 2:
                return False
            else:
                print('Pick a value from 1 to 2.')
        except ValueError:
            print('Value Error')


def reroll_computer():
    choice = random.randint(1, 2)
    print('The computer is debating on rolling again or passing. . .\n')
    time.sleep(1)
    if choice == 1:
        return True
    else:
        return False



def user_play(user_score):
    input('Press "ENTER" to roll the dice!\n')
    while True:
        roll_1, roll_2 = random.randint(1, 6), random.randint(1, 6)
        user_score += roll_1 + roll_2
        dice1, dice2 = draw_dice(roll_1, roll_2)
        print(dice1)
        time.sleep(0.7)
        print(dice2)
        time.sleep(0.7)
        if roll_1 == 1 and roll_2 == 1:
            user_score = 0
            print(bold(
                f'(User Score: {font_green(user_score)})') + ' You rolled double 1, your score is reset to zero.\n')
            time.sleep(1)
            return user_score

        elif roll_1 == 1 or roll_2 == 1:
            user_score -= roll_1 + roll_2
            print(bold(
                f'(User Score: {font_green(user_score)})') + ' Your turn ends. You rolled a 1, subtracting the score you earned.\n')
            time.sleep(1)
            return user_score
        elif user_score >= 100:
            return user_score
        else:
            print(bold(f'(User Score: {font_green(user_score)})') + ' You rolled a ' + bold(roll_1) + ' and ' + bold(roll_2)
                  + '. You may continue to roll . . .\n Select an option below:')
            reroll = reroll_user()
            if not reroll:
                print("You have chosen to pass the turn to the computer\n")
                time.sleep(1)
                return user_score
            else:
                print('You have chosen to continue to roll... good luck!\n')
                time.sleep(1)



def computer_play(computer_score):
    while True:
        input('The computer is rolling the dice! Press "ENTER" to continue . . . ')
        time.sleep(0.5)
        roll_1, roll_2 = random.randint(1, 6), random.randint(1, 6)
        computer_score += roll_1 + roll_2
        dice1, dice2 = draw_dice(roll_1, roll_2)
        print(dice1)
        time.sleep(0.7)
        print(dice2)
        time.sleep(0.7)
        if roll_1 == 1 and roll_2 == 1:
            computer_score = 0
            print(bold(f'(Computer Score: {font_red(computer_score)}) ') +
                  'Computers turn ends. It rolled double 1, its score is reset to zero.')
            time.sleep(1)
            return computer_score
        if roll_1 == 1 or roll_2 == 1:
            computer_score -= roll_1 + roll_2
            print(bold(f'(Computer Score: {font_red(computer_score)}) ') +
                  'Computers turn ends. It rolled a 1, subtracting the score it earned.')
            time.sleep(1)
            return computer_score
        elif computer_score >= 100:
            return computer_score
        else:
            time.sleep(1)
            print(bold(f'(Computer Score: {font_red(computer_score)}) ') + 'Computer rolled a ' + bold(roll_1) + ' and ' + bold(roll_2) + ''
                  + '. It may continue to roll.')
            reroll = reroll_computer()
            if not reroll:
                print("The computer has chosen to pass the turn to the you.\n")
                time.sleep(1)
                return computer_score
            else:
                time.sleep(1)


def determine_winner(user_score, computer_score):
    """ Determines the winner based on a score of 100. """
    # dictionary of winners, will return user, computer or none
    WINNERS = {1:'You', 2:'The Computer', 3:'none'}
    if user_score >= (WINNING_SCORE):
        winner = 1
    elif computer_score >= (WINNING_SCORE):
        winner = 2
    else:
        winner = 3

    return WINNERS.get(winner)


def display_results(user_score, computer_score):
    print(bold('User Score: ') + font_green(f'{user_score}'))
    print(bold('Computer Score: ') + font_red(f'{computer_score}\n'))


def main():
    #welcome
    u_score, c_score = 0, 0
    # loop until player reaches or passes the winning score of 100
    while u_score <= WINNING_SCORE and c_score <= WINNING_SCORE:
        # users turn
        u_score = user_play(u_score)
        display_results(u_score, c_score)
        winner = determine_winner(u_score, c_score)
        if winner != 'none':
            print(f'{winner} have won the game!')
            break

        # computers turn
        c_score = computer_play(c_score)
        display_results(u_score, c_score)
        winner = determine_winner(u_score, c_score)
        if winner != 'none':
            print(f'{winner} has won the game!')
            break

main()
'''
user_score = user_play(10)
display_results(user_score, 100)
winner = determine_winner(user_score, 10)
if winner != 'none':
    print(f'{winner} has won the game')
computer_score = computer_play(10)
computer_play(com)
'''