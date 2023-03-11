# Patryk Kostek
# Lab 6 Problem 1
'''

Design and implement a program that allows the user to translate sentences into Pig Latin.  Pig Latin, or
"Igpay Atinlay" is a language game in which English words are altered, usually by adding a fabricated suffix or by
moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic
syllable to create such a suffix.  The user should be allowed to enter a word, phrase or sentence (including
punctuation and capitalization) from the keyboard.  The application should display the translated sentence and allow the
user to continue the process as long as desired.

1. These are the translation rules I'd like you to use in your program:

2. Words that begin with a vowel will append "way" at the end of the word.  apple - > appleway

3. Words that begin with a consonant will move the consonant to the end of the word and add "ay".  dog -> ogday

4. Words that begin with multiple consonants will move all of the beginning consonants to the
   end of the word and add "ay. three -> eethray

5. Words that begin with a capital letter should be translated and the
   first letter of the translated word should be capitalized.  Cooper -> Oopercay

6. Words that end with punctuation should be translated and the punctuation should be moved to the end of the
   translated word.  Wow! -> Owway! Capitalization and punctuation in the middle of a word can be ignored.

7. Spaces between words in a sentence should be placed between the translated words in a translated sentence.
apple dog three Cooper Wow!

IPO Chart:
Input
    user_input, play_again
Processing
    for each word
        vowels found, consonants found, multi-con start found, capital found, pronounce found
    for each word
        process changes based what was found
Output
    translated
Example
    apple dog three Cooper Wow! == appleway ogday eethray Oopercay Owway!
'''


import time


class TextModifier:
    """ Class defining font styling for the rest of the program. """
    def bold(self, text):
        """
        Makes the text bold
        :param text:
        :return: bold text
        """
        return '\033[1m' + text + '\033[0m'

    def center(self, text):
        """
        Centers text with new line check. Must be center-most style.
        :param text:
        :return:
        """
        # defining and calculating line spacing and if start with \n
        starts_with_newline, ends_with_newline = text.startswith('\n'), text.endswith('\n')
        text_length = len(text)
        spacing = (text_length // 2)

        # if statement looking for if text starts with new line character
        if starts_with_newline or ends_with_newline:
            text = text.replace('\n', ' ')
            centered_text = (' ' * spacing) + text + (' ' * spacing)
            return centered_text

        # else statement passing when did not find new line character
        else:
            centered_text = (' ' * spacing) + text + (' ' * spacing)
            return centered_text


def welcome():
    """
    Prints initial welcome message and instructions.
    :return:
    """
    # defining message strings
    welcome_message =\
        'Welcome to the Pig Latin Translator'
    instruct_message =\
        'Instructions: Please enter a word or phrase you would like translated.'
    continue_message =\
        'Press "ENTER" to continue. . .\n>'

    # printing messages for the user
    print(f'\n{t.bold(t.center(welcome_message))}\n')
    input(f'{continue_message}')
    print(f'\n{instruct_message}')


def is_valid(phrase):
    """
    Checks for digits and makes user try again.
    :param phrase:
    :return: True/False
    """
    isdigit_string = f'\nPlease enter a word without digits. You entered "{phrase}".\n'
    for char in phrase:
        if char.isdigit():
            # debug: print('Return: False')
            print(t.bold(isdigit_string))
            return False
    # returns the flag to the main console
    return True


def find(find_list, item):
    """
    Finds in a string based on find list.
    :param find_list:
    :param item:
    :return: found results:
    """
    found_list = []
    for char in item:
        if char in find_list:
            found_list.append(char)
    return found_list


def find_multi_con(word):
    """
    Looks if word starts with a multi-consonant.
    :param word:
    :return: True/False
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    num_consonants = 0
    for char in word:
        if char in vowel_list:
            return False
        num_consonants += 1
    return num_consonants >= 2


def gather_input():
    """
    Gathers the user's input.
    :return: user_input:
    """
    gather_message = '[Translate]: '
    user_input = input(t.bold(gather_message))
    return user_input


def get_play(msg):
    """
    Asks user if play again.
    :param msg:
    :return: True/False
    """
    choices = ['yes', 'no']
    choice = input(t.bold(msg))
    if choice.lower() not in choices:
        print("I don't understand . . . please choose: (yes/no)\n")
        return get_play(msg)
    elif choice.lower() == choices[0]:
        return True
    else:
        return False


def split_words(msg):
    """
    Splits words into words and returns in a list of words.
    :param msg:
    :return: split_list
    """
    split_list = msg.split()
    return split_list


def translate(user_input):
    """
    Translates the word into pig latin.
    :param user_input:
    :return: word_list joined.
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    con_list = [char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in vowel_list]
    pron_list = ['!', '?', '.', ',', ':', ';']
    v_mod = 'way'
    c_mod = 'ay'
    word_list = split_words(user_input)
    print(f'{t.bold("Words Found:")} {len(word_list)}\n')
    time.sleep(1)
    for i in range(len(word_list)):
        word = word_list[i]
        capitalized_word_found = word[0].isupper()
        word = word_list[i].lower()
        vowels_found = find(vowel_list, word)
        consonants_found = find(con_list, word)
        multi_consonants_found = find_multi_con(word)
        pronounce_mark_found = find(pron_list, word)
        print(f'{t.bold("Word:")} {word_list[i]}\n'
              f'{t.bold("Vowel Found:")} {vowels_found}\n'
              f'{t.bold("Consonants Found:")} {consonants_found}\n'
              f'{t.bold("Multi-Con Start Found:")} {multi_consonants_found}\n'
              f'{t.bold("Pronounce Mark Found:")} {pronounce_mark_found}\n'
              f'{t.bold("Capitalized?:")} {capitalized_word_found}\n')
        time.sleep(0.5)

        if vowels_found:
            for vowel in vowel_list:
                if word.startswith(vowel):
                    word = f'{word}{v_mod}'

        if multi_consonants_found:
            while len(word) > 0 and word[0] in con_list:
                word = word[1:] + word[0]
            word = f'{word}{c_mod}'

        if consonants_found:
            for consonant in con_list:
                if word.startswith(consonant):
                    word = (word[1:] + consonant)
                    word = f'{word}{c_mod}'

        if capitalized_word_found:
            word = word.capitalize()

        if pronounce_mark_found:
            for mark in pronounce_mark_found:
                word = word.replace(mark, '')
                word = word + ''.join(pronounce_mark_found)
        word_list[i] = word
    return ' '.join(word_list)


def main1():
    welcome()                               # print welcome message
    play_again = True
    while play_again:
        valid_state = False                     # local variable initialization
        user_input = ''
        while valid_state is not True:          # if not valid answer loop
            user_input = gather_input()
            valid_state = is_valid(user_input)

        else:                                   # main program
            translated = translate(user_input)
            print(t.center(t.bold('----Translation----')))
            print(translated)
            play_again = get_play('\nWould you like you play again? (yes/no):\n>')
    exit()


if __name__ == '__main__':
    t = TextModifier()
    main1()

