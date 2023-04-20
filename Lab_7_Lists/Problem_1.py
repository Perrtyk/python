# Patryk Kostek
# Lab 7 Problem 1
'''

Design and implement a program that simulates Magic 8-Ball.  The Magic 8-Ball is a plastic sphere made
to look like an eight-ball, that is used for fortune-telling or seeking advice.  The program should
allow a user to enter a question from the keyboard.  The program should respond to the question by
selecting one of 20 pre-programmed responses.  The user should be allowed to ask questions repeatedly
in one program run.

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


def welcome():
    """
    Prints the initial welcome screen, requires enter pressed to continue.
    :return:
    """
    title = list()
    title.append("  __  __                   _        \n")
    title.append(" |  \/  |                 (_)       \n")
    title.append(" | \  / |   __ _    __ _   _    ___ \n")
    title.append(" | |\/| |  / _` |  / _` | | |  / __|\n")
    title.append(" | |  | | | (_| | | (_| | | | | (__ \n")
    title.append(" |_|  |_|  \__,_|  \__, | |_|  \___|\n")
    title.append("   ___      ____    __/ |   _   _   \n")
    title.append("  / _ \    |  _ \  |___/   | | | |  \n")
    title.append(" | (_) |   | |_) |   __ _  | | | |  \n")
    title.append("  > _ <    |  _ <   / _` | | | | |  \n")
    title.append(" | (_) |   | |_) | | (_| | | | | |  \n")
    title.append("  \___/    |____/   \__,_| |_| |_|  \n")
    title.append("\n")
    title.append(f"By: {bold('Patryk Kostek')}, Lane Community College\n")
    print(''.join(title))
    input(f"Press '{bold(green('Enter'))}' to continue . . .\n>")
    clear_screen()


def spawn_ball():
    """
    Spawns ascii art for the 8 ball.
    :return:
    """
    ball = list()
    ball.append('''  .-"""-.  \n''')
    ball.append(''' /   _   \ \n''')
    ball.append('''|   (8)   |\n''')
    ball.append(''' \   ^   / \n''')
    ball.append('''  '-...-'  \n''')
    return ''.join(ball)


def spawn_response(response):
    """
    Spawns the ascii art for the chat bubble for the 8 ball.
    :param response:
    :return:
    """
    chat_bubble = list()
    chat_bubble.append(f"    / \          \n")
    chat_bubble.append(f" ／￣ 　￣￣￣￣￣￣ \n")
    chat_bubble.append(f" |　{yellow(bold(response))}    \n")
    chat_bubble.append(f" ＼＿＿＿＿＿＿＿＿  ")
    return ''.join(chat_bubble)


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


def spawn_ui(response):
    """
    spawns complete UI with 8-ball and response bubble
    :param response:
    :return:
    """
    print(spawn_ball())
    print(spawn_response(response))


def ball_response():
    """
    Pre-programmed responses that get randomly generated.
    :return: final_response:
    """
    rand_response = random.randint(0, 19)
    responses = [("affirmative", "It is certain."), ("affirmative", "It is decidedly so."),
                 ("affirmative", "Without a doubt."), ("affirmative", "Yes definitely."),
                 ("affirmative", "As I see it, yes."), ("affirmative", "Most likely."),
                 ("affirmative", "Yes."), ("affirmative", "Signs point to yes."),
                 ("affirmative", "Outlook good."), ("affirmative", "You may rely on it."),
                 ("non_committal", "Reply hazy, try again."), ("non_committal", "Ask again later."),
                 ("non_committal", "Better not tell you now."), ("non_committal", "Cannot predict now."),
                 ("non_committal", "Concentrate and ask again."), ("negative", "Don't count on it."),
                 ("negative", "My reply is no."), ("negative", "My sources say no."),
                 ("negative", "Outlook not so good."), ("negative", "Very doubtful.")]
    color_response = []
    for i, response in enumerate(responses):
        if response[0] == "affirmative":
            color_response.append(green(response[1]))
        elif response[0] == "non_committal":
            color_response.append(yellow(response[1]))
        else:
            color_response.append(red(response[1]))

    final_response = color_response[rand_response]
    return final_response


def gather_input():
    """
    Gather's user's input but does not do anything other the validation.
    :return:
    """
    user_input = input(f'\n[{bold("Question")}]: ')
    digit_count = 0
    alpha_count = 0

    # Loop through each character in the input string
    for char in user_input:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            alpha_count += 1

    if user_input == '':
        print(f'\n{bold(red("Error:"))} Question cannot be blank.')
        gather_input()
    elif not user_input.endswith('?'):
        print(f'\n{bold(red("Error:"))} Please end statement with a "?" as it has to be a question.')
        gather_input()
    elif digit_count > alpha_count:
        print(f'\n{bold(red("Error:"))} It seems like there is more digits than letters, are you sure this is a question?')
        gather_input()
    else:
        pass


def main1():
    """
    Runs main program function
    :return: 
    """
    welcome()
    response = 'Would you like to ask me a question?'
    play = True
    while play:
        spawn_ui(response)
        gather_input()
        response = ball_response()
        clear_screen()
        spawn_ui(response)
        play = get_play('Would you like to ask me another question?\n1 - Yes\n2 - No\n>')
        clear_screen()
        response = "What is your next question?"
    else:
        end_string = 'Thank you trying out Magic 8 Ball!'
        print(f'{bold(end_string)}')


if __name__ == '__main__':
    main1()

