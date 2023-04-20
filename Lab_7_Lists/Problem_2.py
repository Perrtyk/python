"""

Design and implement a program that simulates a lottery.  The user should be asked to enter 5 integers between 1 and 69
and an additional integer between 1 and 26.  The computer will generate random numbers, 5 between 1 and 69 and 1 between
1 and 26, for the winning lottery ticket.  The program should display the winning lottery ticket as well as the user's
results.  The image at the right gives the possible prizes.

"""
import time
import random as r

def clear_screen():
    """
    Clears the frame.
    :return:
    """
    print('\n' * 40)


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


def get_winning_ticket():
    """
    Randomly generates a ticket.
    :return:
    """
    match_tkt = []
    for i in range(5):
        match_tkt.append(str(r.randint(1, 69)))
    match_tkt.append(str(r.randint(1, 26)))
    return match_tkt


def get_ticket():
    """
    Gathers input from user for their ticket numbers.
    :return:
    """
    tkt_list = []
    for i in range(1, 6):
        clear_screen()
        print('\n'.join(display_ticket_frame(tkt_list)))
        tkt = 0
        msg = f"{bold(f'[Ticket #{i}]')} (1-69): "

        valid_input = False
        while not valid_input:
            print()
            tkt = (input(msg))
            valid_input = validation(1, 69, tkt)
        tkt_list.append(tkt)

    valid_input = False
    while not valid_input:
        clear_screen()
        print('\n'.join(display_ticket_frame(tkt_list)))
        print()
        msg = f"{bold(f'[Powerball #6]')} (1-26): "
        tkt = (input(msg))
        valid_input = validation(1, 26, tkt)
    tkt_list.append(tkt)

    for loop in range(3):
        for i in range(1, 4):
            clear_screen()
            print('\n'.join(display_ticket_frame(tkt_list)), f'\nSubmitting your ticket {". " * i}')
            time.sleep(0.25)
    return tkt_list


def validation(min_val, max_val, val):
    """
    Validation for input from user given the minimum, maximum and value chosen.
    :param min_val:
    :param max_val:
    :param val:
    :return:
    """
    try:
        if int(val) >= min_val and int(val) <= max_val:
            print('min max values: true')
            return True
        elif not val.isdigit():
            print('val.isdigit(), false')
            return False
        else:
            print('else statement')
            return False
    except (ValueError, TypeError) as e:
        print(e)
        return False


def calc_prize(match, pb):
    """
    Calculates the get prize based on matches with the winning ticket.
    :param match:
    :param pb:
    :return:
    """
    prize = '0.00'
    if match is None:
        if pb is None:
            prize = '0.00'
        else:
            prize = '4.00'
    else:
        matches = len(list(match))
        print(matches)
        if matches == 1 and pb is not None:
            prize = '4.00'
        elif matches == 2 and pb is not None:
            prize = '7.00'
        elif matches == 3 and pb is None:
            prize = '7.00'
        elif matches == 3 and pb is not None:
            prize = '100.00'
        elif matches == 4 and pb is None:
            prize = '100.00'
        elif matches == 4 and pb is not None:
            prize = '50,000.00'
        elif matches == 5 and pb is None:
            prize = '1,000,000.00'
        elif matches == 5 and pb is not None:
            prize = f'{bold("33,000,000.00")} JACKPOT ! ! !'
    return prize


def get_play(msg):
    """
    Asks user if play again.
    :param msg:
    :return: True/False
    """
    choices = ['1', '2']
    choice = input(bold(msg))
    if choice not in choices:
        clear_screen()
        print("I don't understand . . . please choose: (1 or 2)\n")
        return get_play(msg)

    elif choice == choices[0]:
        return True

    else:
        return False


def display_welcome_frame():
    """
    Prints welcome frame and instructions.
    :return:
    """
    title = []
    title.append(bold('  ______   ______     __     __     ______     ______     \n '))
    title.append(bold('/\  == \ /\  __ \   /\ \  _ \ \   /\  __\    /\  == \    \n '))
    title.append(bold('\ \  _-/ \ \ \/\ \  \ \ \/ ".\ \  \ \  __\   \ \  __<    \n '))
    title.append(bold(' \ \_\    \ \_____\  \ \__/".~\_\  \ \_____\  \ \_\ \_\ \n '))
    title.append(bold('  \/_/     \/_____/   \/_/   \/_/   \/_____/   \/_/ /_/  \n '))
    title.append(bold(' ______     ______     __         __                     \n '))
    title.append(bold('/\  == \   /\  __ \   /\ \       /\ \                    \n '))
    title.append(bold('\ \  __<   \ \  __ \  \ \ \____  \ \ \____               \n '))
    title.append(bold(' \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\              \n '))
    title.append(bold('  \/_____/   \/_/\/_/   \/_____/   \/_____/             \n' ))
    title.append('\n')
    title.append(f'By: {bold("Patryk Kostek")}, Lane Community College\n')
    print(''.join(title))
    print()
    input("Press 'Enter' to continue . . .")


def display_ticket_frame(tkt_list):
    """
    Displays the ticket frame for choosing a ticket number.
    :param tkt_list:
    :return:
    """
    picture = []
    tkt_index = f"______________________________\n" + \
                f"{bold(yellow(' 01   02   03   04   05   PB  '))}"
    for i in range(1, 7):
        try:
            picture.append(f"[{int(tkt_list[i-1]):02d}] ")
        except IndexError:
            picture.append(f"[  ] ")
    picture.append("\n------------------------------")
    picture = ''.join(picture)
    return tkt_index, picture


def display_match_frame(p_ticket, m_ticket, matches, p_match):
    """
    Builds and displays the match results frame.
    :param p_ticket:
    :param m_ticket:
    :param matches:
    :param p_match:
    :return:
    """
    print(f"\n{bold('   Your numbers:')} {', '.join(f'{num:>2}' for num in p_ticket[:5])}   {bold('Powerball:')} {p_ticket[5]}")
    print(f"{bold('Winning numbers:')} {', '.join(m_ticket[:5])}   {bold('Powerball:'):<5} {m_ticket[5]}")
    print(f"{bold('        Matches:')} {matches}")
    if p_match is not None:
        print(f"{bold('Powerball match:')} {green(p_match)}")
    else:
        print(f"{bold('Powerball match:')} {p_match}")


def main2():
    """
    Runs the main program.
    :return:
    """
    display_welcome_frame()
    play_again = True
    while play_again:
        player_ticket = get_ticket()
        match_ticket = get_winning_ticket()
        matches = set(player_ticket[:5]) & set(match_ticket[:5])
        if not matches:
            matches_copy = None
            matches_msg = ''
        else:
            matches_copy = matches
            matches_msg = ', '.join(matches)
            matches_msg = green(matches_msg)

        if player_ticket[5] == match_ticket[5]:
            p_match = match_ticket[5]
            p_match_msg = p_match
            p_match = green(p_match)
        else:
            p_match = None
            p_match_msg = ''

        display_match_frame(player_ticket, match_ticket, matches_msg, p_match_msg)
        input('\nPress "Enter" to see your prize!')
        prize = calc_prize(matches_copy,p_match)
        print(f"You won ${prize}.\n")
        time.sleep(2)
        play_again = get_play("Would you like to buy another ticket?\n1 - Yes\n2 - No\n>")


if __name__ == '__main__':
    main2()