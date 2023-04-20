import random
import time


# Define pairs of synonyms
synonyms = [['happy', 'glad'], ['angry', 'mad'], ['big', 'large'], ['small', 'little'], ['fast', 'quick'],
            ['smart', 'intelligent'], ['funny', 'humorous'], ['hard', 'difficult'], ['easy', 'simple'], ['old', 'ancient']]
flat_synonym = [word for sublist in synonyms for word in sublist]
random.shuffle(flat_synonym)
random_synonym = [list(x) for x in zip(*[iter(flat_synonym)]*2)]


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


def clear_screen():
    """
    Clears the frame.
    :return:
    """
    print('\n' * 40)


def welcome():
    """
    Prints initial welcome frame and instructions.
    :return:
    """
    title = list()
    print('\n' * 20)
    title.append("   ▄████████    ▄█    █▄     ▄█  ███▄▄▄▄      ▄█   ▄█▄    ▄████████  ▄█ \n")
    title.append("  ███    ███   ███    ███   ███  ███▀▀▀██▄   ███ ▄███▀   ███    ███ ███ \n")
    title.append("  ███    █▀    ███    ███   ███▌ ███   ███   ███▐██▀     ███    █▀  ███▌\n")
    title.append("  ███         ▄███▄▄▄▄███▄▄ ███▌ ███   ███  ▄█████▀     ▄███▄▄▄     ███▌\n")
    title.append("▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ███   ███ ▀▀█████▄    ▀▀███▀▀▀     ███▌\n")
    title.append("         ███   ███    ███   ███  ███   ███   ███▐██▄     ███    █▄  ███ \n")
    title.append("   ▄█    ███   ███    ███   ███  ███   ███   ███ ▀███▄   ███    ███ ███ \n")
    title.append(" ▄████████▀    ███    █▀    █▀    ▀█   █▀    ███   ▀█▀   ██████████ █▀  \n")
    title.append("                                             ▀\n")
    title.append("   ▄████████ ███    █▄   ▄█       ▄█    ▄████████    ▄█   ▄█▄ ███    █▄ \n")
    title.append("  ███    ███ ███    ███ ███      ███   ███    ███   ███ ▄███▀ ███    ███\n")
    title.append("  ███    █▀  ███    ███ ███▌     ███   ███    ███   ███▐██▀   ███    ███\n")
    title.append("  ███        ███    ███ ███▌     ███   ███    ███  ▄█████▀    ███    ███\n")
    title.append("▀███████████ ███    ███ ███▌     ███ ▀███████████ ▀▀█████▄    ███    ███\n")
    title.append("         ███ ███    ███ ███      ███   ███    ███   ███▐██▄   ███    ███\n")
    title.append("   ▄█    ███ ███    ███ ███      ███   ███    ███   ███ ▀███▄ ███    ███\n")
    title.append(" ▄████████▀  ████████▀  █▀   █▄ ▄███   ███    █▀    ███   ▀█▀ ████████▀ \n")
    title.append("                             ▀▀▀▀▀▀                 ▀                   \n")
    print(''.join(title))
    print(f"By: {bold('Patryk Kostek')}, Lane Community College\n")
    input('Press "Enter" to continue. . .')
    clear_screen()
    print(f'{bold("---Instructions---")}\n\nShinkei Suijaku is a Japanese matching game where players flip over two cards\n'
          f'at a time to find matching pairs. The player with the most pairs at the end\nof the game wins.\n')
    input('Press "Enter" to continue. . .')
    print('Good luck!')
    time.sleep(2)


def create_gameboard(revealed, prev_choice_index, u_score, c_score):
    """
    Prints the gamebaord frame given variables
    :param revealed:
    :param prev_choice_index:
    :param u_score:
    :param c_score:
    :return:
    """
    print(f"{bold(green(f'User Score: {u_score}'))} | {bold(red(f'Computer Score: {c_score}'))}")
    if prev_choice_index != '':
        print(f'Previous Card: {bold(yellow(prev_choice_index))}\n')
    else:
        print(f'Previous Card: ')
    board = []
    # builds the board based on revealed cards
    for i in range(1, 21):
        if i in revealed:
            card = '|  |'
        else:
            card = f'|{i:02d}|'
        board.append(card)
    for i in range(0, 20, 5):
        print(' '.join(board[i:i+5]))


def pick_card(revealed_list, previous_pick):
    """
    Prompts the user to pick a card with validation.
    :param revealed_list:
    :param previous_pick:
    :return:
    """
    while True:
        try:
            pick = int(input('\n[Card Number]: '))
            if pick < 1 or pick > 20:
                print('Please choose a value between 1 and 20.')
            elif pick in revealed_list:
                print(f'That card is already revealed ({pick}). Please pick another card.')
            elif pick == previous_pick:
                print(f'That card is already revealed ({pick}). Please pick another card.')
            else:
                return pick
        except ValueError:
            print('Input cannot be a letter or empty.')


def c_pick_card(revealed_list):
    """
    Randomly generates computer response with validation.
    :param revealed_list:
    :return:
    """
    try:
        pick1 = random.choice([i for i in range(1, 21) if i not in revealed_list])
        pick2 = random.choice([i for i in range(1, 21) if i not in revealed_list and i != pick1])
        return pick1, pick2
    except IndexError:
        pick1 = random.randint(1, 20)
        pick2 = random.randint(1, 20)
        return pick1, pick2


def reveal(word_list, n):
    """
    Reveals the word based on index and list.
    :param word_list:
    :param n:
    :return:
    """
    index = (n - 1) // 2  # index of the list containing the word
    word_index = (n - 1) % 2  # index of the word within the list
    word = word_list[index][word_index]
    word_reveal = f'|{n:02d}| - {word}'
    return word, word_reveal


def check_match(pair, match_list):
    """
    Checks the pair against a match list, returns true or false.
    :param pair:
    :param match_list:
    :return:
    """
    if pair in match_list:
        return True
    elif [pair[1], pair[0]] in match_list:
        return True
    else:
        return False


def main():
    """
    Runs the main function.
    :return:
    """
    # initialize the game frame
    revealed = []  # list of revealed cards
    user_score, comp_score = 0, 0
    user_turn = True
    comp_turn = False
    welcome()
    # while loop, 2 conditions to finish the game, len of revealed cards and score combined.
    while user_score + comp_score < 10 or len(revealed) < len(flat_synonym):
        while user_turn:
            clear_screen()
            create_gameboard(revealed, '', user_score, comp_score)
            pick1 = pick_card(revealed, '')
            pick1_word, pick1_reveal = reveal(random_synonym, pick1)  # reveals user's answer
            revealed.append(pick1)
            clear_screen()

            create_gameboard(revealed, pick1_reveal, user_score, comp_score)
            pick2 = pick_card(revealed, pick1)
            pick2_word, pick2_reveal = reveal(random_synonym, pick2)
            revealed.append(pick2)
            clear_screen()

            create_gameboard(revealed, pick2_reveal, user_score, comp_score)
            pick_pair = [pick1_word, pick2_word]
            match_result = check_match(pick_pair, synonyms)
            print(f'\nYou Chose: {bold(yellow(pick1_reveal.capitalize()))} and {bold(yellow(pick2_reveal.capitalize()))}')

            if match_result is True:
                print(f'{bold("Matched Result")}: You {bold(green("matched"))} {pick1_reveal} and {pick2_reveal}')
                user_score += 1
                input('It is still your turn. Press "Enter" to continue. . .')
                clear_screen()
            else:
                print(f'\n{bold("Matched Result")}: {bold(red("None"))}, your turn is now over.')
                input('\nPress "Enter" to continue. . .')
                revealed.remove(pick1)
                revealed.remove(pick2)
                clear_screen()
                user_turn = False
                comp_turn = True
        while comp_turn:
            c_pick1, c_pick2 = c_pick_card(revealed)
            revealed.append(c_pick1)
            revealed.append(c_pick2)
            c_pick1_word, c_pick1_reveal = reveal(random_synonym, c_pick1)
            c_pick2_word, c_pick2_reveal = reveal(random_synonym, c_pick2)
            c_pick_pair = [c_pick1_word, c_pick2_word]
            match_result = check_match(c_pick_pair, synonyms)
            create_gameboard(revealed, '', user_score, comp_score)
            print(f'\nComputer Chose: {bold(yellow(c_pick1_reveal.capitalize()))} and {bold(yellow(c_pick2_reveal.capitalize()))}')
            time.sleep(1)

            if match_result is True:
                print(f'\n{bold("Matched Result")}: Computer {bold(green("matched"))} {c_pick1_reveal.capitalize()} and {c_pick2_reveal.capitalize()}')
                comp_score += 1
                input(f'It is still the computers turn. Press "Enter" to continue. . .')
                clear_screen()
            else:
                print(f'\n{bold("Matched Result")}: {bold(red("None"))}, the computers turn is now over.')
                time.sleep(1)
                revealed.remove(c_pick1)
                revealed.remove(c_pick2)
                input('It is your turn. Press "Enter" to continue. . .')
                clear_screen()
                user_turn = True
                comp_turn = False

    print('Congratulations, you have finished the game!')
    if user_score > comp_score:
        print(f'You are the winner. Your score was {bold(green(user_score))} and the computers was {bold(red(comp_score))}.')
        input('Press "Enter" to exit.')
    else:
        print(f'You lost! Your score was {bold(green(user_score))} and the computers was {bold(red(comp_score))}. ')
        input('Press "Enter" to exit.')


if __name__ == '__main__':
    main()

"""

This problem gave me many issues due to initially using lists in lists as opposed to two lists and using the index to
find the pairs. This led my down the journey of dictionaries which I was not comfortable with. I eventually found a way
to make lists of lists work with the synonyms by flattening the lists to randomize it and rejoining it in it's original
format. I think used the original synonym list as my answer key for my pairs and used the randomized list for generation.

"""