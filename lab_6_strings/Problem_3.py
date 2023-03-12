# Patryk Kostek
# Lab 6 Problem 3
'''

Design and implement a program that allows the user to play a game similar to Wheel of Fortune.
Wheel of Fortune is a popular word game in which the player is given a category (Movie, Famous Person)
and some number of blanks representing each character in the name of the movie or person.  The user
guesses one letter at a time and the program updates the display to include the letter where it appears
in the name.  The program should also display any character that was guessed incorrectly as well as the
number of incorrect guesses remaining.  The game ends when the user has filled in all of the characters
or has guessed incorrectly 5 times for a particular puzzle.  The user should be allowed to play puzzles
repeatedly and the program should keep track of how many puzzles the user has completed successfully.

'''

import random


def clear_screen(num_lines=50):
    """Clears the terminal screen by printing empty lines."""
    for _ in range(num_lines):
        print()


def bold(text):
    """
    Returns text in bold.
    :param text:
    :return: bold_text:
    """
    # Define a string with bold text using ANSI escape codes
    bold_text = "\033[1m" + text + "\033[0m"
    # Return the bold text
    return bold_text


def red(text):
    """
    Returns text in red font.
    :param text:
    :return: red_text:
    """
    # Define a string with red text using ANSI escape codes
    red_text = "\033[31m" + text + "\033[0m"
    # Return the red text
    return red_text


def green(text):
    """
    Returns text in yellow font.
    :param text:
    :return: yellow_text:
    """
    # Define a string with yellow text using ANSI escape codes
    green_text = ('\033[32m' + text + '\033[0m')
    # Return the yellow text
    return green_text


def yellow(text):
    """
    Returns text in yellow font.
    :param text:
    :return: yellow_text:
    """
    # Define a string with yellow text using ANSI escape codes
    yellow_text = "\033[33m" + text + "\033[0m"
    # Return the yellow text
    return yellow_text





def welcome(wins, losses):
    """
    Prints the welcome message, instructions and score.
    :param wins:
    :param losses:
    :return:
    """
    clear_screen(25)
    title = []
    title.append(" __    __  _                  _             __      __               _                        \n")
    title.append("/ / /\ \ \| |__    ___   ___ | |     ___   / _|    / _|  ___   _ __ | |_  _   _  _ __    ___  \n")
    title.append("\ \/  \/ /| '_ \  / _ \ / _ \| |    / _ \ | |_    | |_  / _ \ | '__|| __|| | | || '_ \  / _ \ \n")
    title.append(" \  /\  / | | | ||  __/|  __/| |   | (_) ||  _|   |  _|| (_) || |   | |_ | |_| || | | ||  __/ \n")
    title.append("  \/  \/  |_| |_| \___| \___||_|    \___/ |_|     |_|   \___/ |_|    \__| \__,_||_| |_| \___| \n")
    title.append(f"                               {green('Wins:')} {wins}       {red('Losses:')} {losses}\n")
    print(f'{bold("".join(title))}')

    print(f"By: {bold('Patryk Kostek')}, Lane Community College\n")
    print(f"You will be given a category and a phrase. Guess the phrase one letter at a time.\n"
          f"You will lose after 5 incorrect attempts... so be careful!\n")
    input(f'Press "Enter" to continue . . .\n')


def init_screen(category, word, found_list, guess_list, attempts):
    """
    Initializes the frame based on parameters.
    :param category:
    :param word:
    :param found_list:
    :param guess_list:
    :param attempts:
    :return:
    """
    clear_screen(25)
    empty_char = '[ ]'
    game_word = ''
    for i, char in enumerate(word.lower()):
        if char == ' ':
            new_char = '   '
            game_word += new_char
        elif char in found_list:
            new_char = f'[{bold(yellow(char))}]'
            game_word += new_char
        else:
            new_char = empty_char
            game_word += new_char

    guess_list = sorted(guess_list)
    for i in range(len(guess_list)):
        if guess_list[i] in found_list:
            guess_list[i] = green(guess_list[i])
        else:
            guess_list[i] = red(guess_list[i])

    print(f'{bold("Category: ")}{category}')
    print(game_word + '\n')
    print(f'   {bold("Guessed Letters:")} {" ".join(guess_list)}')
    print(f'{bold("Incorrect Attempts:")} {attempts} / 5\n')


def get_puzzle():
    """This function returns a tuple (Category, Phrase) that can be used to play a simple game of like
      Wheel of Fortune."""
    puzzles = [("Famous People", "Abraham Lincoln"), ("Famous People", "Oprah Winfrey"),
               ("Famous People", "Will Smith"),
               ("Famous People", "Marilyn Monroe"),
               ("Place", 'Used Car Lot'),
               ("Place", 'Hotel Lobby'),
               ("Phrase", 'All the Time in the World'),
               ("Phrase", 'Tax Season Already'),
               ("Phrase", 'Hang In There'),
               ("Phrase", 'First Things First')]
    index = random.randint(0, len(puzzles) - 1)
    return puzzles[index]


def get_guess(guess_list):
    """
    Gathers the user's input by getting their guess. Provides validation.
    :param guess_list:
    :return: guess.lower()
    """
    while True:
        guess = input(f'[{bold(green("Letter Guess"))}]: ')
        if len(guess) != 1:
            print(f'{bold(red("Amount Error:"))} Please select only one letter at a time.\n')

        elif not guess.isalpha():
            print(f'{bold(red("Value Error:"))} Please select a letter from A to Z.\n')

        elif guess.lower() in guess_list:
            print(f'{bold(red("Duplicate Error:"))} Please select a letter you have not selected before.\n')

        else:
            return guess.lower()


def get_play(msg):
    """
    Asks user if play again.
    :param msg:
    :return: True/False
    """
    choices = ['1', '2']
    choice = input(bold(msg))
    if choice not in choices:
        print("I don't understand . . . please choose: (1 or 2)\n")
        return get_play(msg)

    elif choice == choices[0]:
        return True

    else:
        return False


def main3():
    """
    Runs the main program with play again loop and score tracking.
    :return:
    """
    wins, losses = 0, 0
    play_again = True
    while play_again:
        attempts = 0
        welcome(wins, losses)
        (category, name) = get_puzzle()
        name_index = set(name.lower().replace(' ', ''))
        found_list, guess_list = [], []
        while True:
            init_screen(category, name, found_list, guess_list, attempts)
            guess = get_guess(guess_list)
            guess_list.append(guess)
            if guess in name_index:
                found_list.append(guess)

            else:
                attempts += 1

            if len(found_list) == len(set(name_index)):
                wins += 1
                print('You win!\n')
                play_again = get_play('Would you like to play another puzzle?\n1. Yes\n2. No\n>')
                break

            elif attempts == 5:
                losses += 1
                print('You lose!\n')
                play_again = get_play('Would you like to play another puzzle?\n1. Yes\n2. No\n>')
                break
    else:
        print(f"                               {green('Wins:')} {wins}       {red('Losses:')} {losses}\n")


# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main3()
