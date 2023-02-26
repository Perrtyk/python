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


WINNING_SCORE = 100


def draw_dice(roll_1, roll_2):
    dice_1 = 0
    dice_2 = 0
    print(dice_1, dice_2)

def reroll_user():
    return

def reroll_computer():
    return


def user_play(user_score):
    return user_score


def computer_play(computer_score):
    return computer_score


def determine_winner(user_score, computer_score):
    WINNERS = {1:'user', 2:'computer', 3:'none'}
    if user_score > 99:
        winner = 1
    elif computer_score > 99:
        winner = 2
    else:
        winner = 3

    return WINNERS.get(winner)


def display_results():
    return

def main():
    string = determine_winner(50, 3)
    print(string)


main()
