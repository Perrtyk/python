"""
Patryk Kostek
Lab 6 Problem 2

Design and implement a program that will allow the user to encode words and phrases using a shift or Ceasar cypher.
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which
each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.For example,
with a right shift of 3, A would be replaced by D, B would become E, and so on. The method is named after
Julius Caesar, who used it in his private correspondence.

IPO Chart:

Input:
    decrypted_phrase, shift_amount
Processing:
    gather decrypted phrase, shift_amount
    encrypt_phrase(shift_amount)
    return encrypted_phrase
Output:
    return encrypted_phrase
"""
import time


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
    Prints welcome message and instructions to the program.
    :return:
    """
    string_list = []
    instruction_list = []
    instruction_list.append(f"Welcome to {bold('Caesars Cipher')}!\n")
    instruction_list.append(f"Please provide us the {red(bold('shift'))} for your encryption as well as"
                            f" the {red(bold('phrase'))} you would like to encrypt.\n")
    instruction_list.append(f'We will encrypt it by shifting the alphabetical values, as Caesar did in 100 B.C. 👽\n')

    string_list.append(f"{yellow('                     ___')}\n")
    string_list.append(f"{yellow('                    ( ((')}\n")
    string_list.append(f"{yellow('                     ) ))')}\n")
    string_list.append(f"{yellow('  .::.              / /(')}\n")
    string_list.append(f" '{red('J')} {yellow('.-;-.-.-.-.-.-|| ((')}::::::::::::::::::::::::::::::::::..\n")
    string_list.append(f"{yellow('(  ( ( ( ( ( ( ( ( |  ))')}   "
                       f"-====-{bold(red('Caesars Cipher'))}-===-     =:=>\n")
    string_list.append(f" `{red('C')} {yellow('`-;-`-`-`-`-`-|| ((')}::::::::::::::::::::::::::::::::::''\n")
    string_list.append(f'''{yellow("  `::'              / /()")}\n''')
    string_list.append(f"{yellow('                    (_((')}\n")
    string_list.append(f"By: {bold('Patryk Kostek')}, Lane Community College\n")

    print(''.join(string_list))
    input('Press "Enter" to continue . . .\n>')
    print('\n' * 15), print(''.join(instruction_list))
    input('Press "Enter" to continue . . .\n>')
    print('\n')


def gather_input():
    """
    Gathers the user input for the processing.
    :return: shift_value, msg, user_choice:
    """
    while True:
        try:
            user_choice = int(input(f'Please select one of the following options:'
                               f'\n1. {bold("Encrypt")}\n2. {bold("Decrypt")}\n>'))
            print('\n')
            if user_choice != 1 and user_choice != 2:
                raise ValueError
            break
        except ValueError:
            print('Value Error: Please select a numerical value from your options above.\n')

    while True:
        try:
            shift_value = int(input(f'[{red(bold("Shift"))}]: '))
            if shift_value < 1:
                raise ValueError
            break
        except ValueError:
            print('Please choose a numerical value that is greater than 0. (Example: 6)\n')

    msg = input(f'[{red(bold("Phrase to Encrypt or Decrypt"))}]: ')
    return shift_value, msg, user_choice


def encrypt_text(msg, shift_value):
    """
    Encrypts the phrase.
    :param msg:
    :param shift_value:
    :return: encrypted_text:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 100 # a - 0, z - 25, loops 100 times for larger shifts
    encrypted_text = ''
    for i in range(len(msg)):
        try:
            if msg[i].isdigit():
                encrypted_text += msg[i]
            elif msg[i].isupper():
                old_char = msg[i].lower()
                old_index = alphabet.index(old_char)
                new_index = (old_index + shift_value) % len(alphabet)
                new_char = alphabet[new_index]
                encrypted_text += new_char.upper()
            elif msg[i] in alphabet:
                old_index = alphabet.index(msg[i])
                new_index = (old_index + shift_value) % len(alphabet)
                new_char = alphabet[new_index]
                encrypted_text += new_char
            else:
                encrypted_text += msg[i]
        except IndexError:
            old_index = alphabet.index(msg[i])
            new_index = (old_index + shift_value) % len(alphabet)
            new_char = alphabet[new_index]
            encrypted_text += new_char
    return encrypted_text


def decrypt_text(msg, shift_value):
    """
    Decrypts the phrase
    :param msg:
    :param shift_value:
    :return: decrypted_text
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 100   # a - 0, z - 25, loops 100 times for larger shifts
    decrypted_text = ''
    for i in range(len(msg)):
        try:
            if msg[i].isdigit():
                decrypted_text += msg[i]
            elif msg[i].isupper():
                old_char = msg[i].lower()
                old_index = alphabet.index(old_char)
                new_index = (old_index - shift_value) % len(alphabet)
                new_char = alphabet[new_index]
                decrypted_text += new_char.upper()
            elif msg[i] in alphabet:
                old_index = alphabet.index(msg[i])
                new_index = (old_index - shift_value) % len(alphabet)
                new_char = alphabet[new_index]
                decrypted_text += new_char
            else:
                decrypted_text += msg[i]
        except IndexError:
            old_index = alphabet.index(msg[i])
            new_index = (old_index - shift_value) % len(alphabet)
            new_char = alphabet[new_index]
            decrypted_text += new_char
    return decrypted_text


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


def main2():
    welcome()
    play_again = True
    while play_again:
        shift, phrase, choice = gather_input()
        if choice == 1:
            encrypted_phrase = encrypt_text(phrase, shift)
            print(f'[{bold(red("Encrypted Phrase"))}]: {bold(encrypted_phrase)}\n')
            time.sleep(1)
            play_again = get_play(f'Would you like to play again? (Select 1 or 2)\n1. {bold("Yes")}\n2. {bold("No")}\n>')
            print('\n')
        else:
            decrypted_phrase = decrypt_text(phrase, shift)
            print(f'[{bold(red("Decrypted Phrase"))}]: {bold(decrypted_phrase)}\n')
            time.sleep(1)
            play_again = get_play(f'Would you like try another phrase? (Select 1 or 2)\n1. {bold("Yes")}\n2. {bold("No")}\n>')
            print('\n')


if __name__ == '__main__':
    main2()
