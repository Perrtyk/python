# Patryk Kostek
# Lab 3 Problem 5
#
'''
    Design and implement a program that allows the user to play Rock Paper Scissors
    (Lizard Spock anyone?)  against the computer.  The user begins by entering either
    Rock, Paper or Scissors at the keyboard.  The computer's move should be implemented
    by generating a random number between 1 and 3.  1 = Rock, 2 = Paper, 3 = Scissors.
    The program should display the user's move as well as the computer's move AND should
    display who won.  It is NOT necessary to validate the input from the user.  Your
    solution should have a function called displayWinner as well as main function.
    displayWinner should have 2 parameters, the user's choice and the computer's choice.
    displayWinner should display each choice as well as who won.  main should generate the
    computer's choice, get the user's choice and call the displayWinner function.


IPO Chart:
    Input
        u_choice
    Processing
        import random library
        define constants 1 = ROCK, 2 = PAPER, 3 = SCISSORS
        define random_num function, generate number 1-3 return as c_choice
        define gather_input function, gathers constant  return as u_choice

        define display_winner(u_choice, c_choice) function
            if u_choice is same as c_choice then
                message is 'It's a Tie!'
            elif u_choice is rock and c_choice is scissors
                message is 'You win, rock beats scissors!
            elif u_choice is scissors and c_choice is paper
                message is 'You win, scissors beats paper!
            elif u_choice is paper and c_choice is rock
                message is 'You win, paper beats rock!
            else print(f'You lose, c_choice beats u_choice!)

        state the welcome message showing instructions
        gather the input
        display the winner using display_winner
    Output
        display the winner.


Algorithm:

     display_winner(u_choice, c_choice) function
        if u_choice is same as c_choice then
            message is 'It's a Tie!'
        elif u_choice is rock and c_choice is scissors
            message is 'You win, rock beats scissors!
        elif u_choice is scissors and c_choice is paper
            message is 'You win, scissors beats paper!
        elif u_choice is paper and c_choice is rock
            message is 'You win, paper beats rock!
        else
            message is "Sorry, you lose!"

     gather_input
        state welcome message
        state instructions
        state the options
        gather input and define u_choice case-insensitive
        return u_choice

     rand_gen
        1, 2, 3 = ROCK, PAPER, SCISSORS
        randomly generate number from 1 through 3 assigned to c_choice
        return c_choice


    main
        display welcome message
        display option selection
        gather input case-insensitive, define u_choice
        run rand_gen, define c_choice
        run display_winner(u_choice, c_choice)
    end main
'''
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
    u_choice = input('Selection: ')
    if u_choice.lower() == 'rock':
        return ROCK
    if u_choice.lower() == 'paper':
        return PAPER
    elif u_choice.lower() == 'scissors':
        return SCISSORS
    else:
        return print('Error:')


#   generates a number and returns it based on two parameters
def rand_gen(min_val, max_val):
    """ randomly generate numbers from min_val to max_val """
#   randomly generates a number and assigns it to the computer's choice
    x = random.randint(min_val, max_val)
#   returns the random number as a variable for later use
    return x


#   defines winning combination for if statement, uses choices to determine winner
def display_winner(u_choice, c_choice):
    """ displays winner in message based in u_choice and c_choice """
    WINNING_COMBINATIONS = [
        (ROCK, SCISSORS),
        (SCISSORS, PAPER),
        (PAPER, ROCK)
    ]
    if u_choice == c_choice:
        message = f"It's a Tie! The computer chose {CHOICES[c_choice]}"
    elif (u_choice, c_choice) in WINNING_COMBINATIONS:
        message = f'You \033[92mwin\033[0m, {CHOICES[u_choice]} beats {CHOICES[c_choice]}!'
    else:
        message = f"Sorry, you \033[91mlose\033[0m!\nYou chose {CHOICES[u_choice]}"\
                  f" and the computer chose {CHOICES[c_choice]}."
    return message


#   runs the main body of the code
def main():
    """ prints welcome statement, instructions, and runs code """
    welcome()
    u_choice = gather_input()
    c_choice = rand_gen(1, 3)
    if u_choice in CHOICES:
        message  = display_winner(u_choice, c_choice)
        print(message)
    else:
        print('Please select an option from the selection.')
    return


#   call main when this file is run
if __name__ == '__main__':
    main()

#   With this problem, I experimented more with lists and variables to try and help me
#   reduce the number of code. Originally, the display_winner function was very long, but
#   I was able to break it down and reduce it using variables and lists.