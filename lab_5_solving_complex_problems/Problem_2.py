# Patryk Kostek
# Lab 5 Problem 2
#
"""
Design and implement a program that asks the user to enter a number and determines if
a number entered by the user is a prime number.  A prime number is a number that is
divisible only by 1 and itself.  2, 3, 5 and 7 are prime numbers.  4 and 9 are not
prime numbers.  Your solution should include a "fruitful" function called isPrime
as well as a main function.  isPrime should have one integer parameter, number
and should return either True or False.  main should get the number from the user,
call isPrime and display an appropriate message on the screen.
Algorithm:
is_prime(num)
    if the num is less than 2 then
        num is false
    else
        for loop to see if number is not prime
            if number not prime
                num is False
            else
                num is True
            end if
        end for
    end if
    retun num as True or False
end is_prime(num)
gather_input(message)
    while true loop
        try to
            get the users input, convert to int
            return the user's input
        if not do
            print error message
        end if
    end while
end gather_input
main():
    welcome message
    define num with gather_input
    is num prime using is_prime(num)
    if num is true then
        define prime message
    else
        define not prime message
    print message
n = gather_input('Please enter your number:  ')
    n = is_prime(n)
    if n is True:
        message = 'Your number is prime!'
    else:
        message = 'Your number is not prime!'
    print(message)
"""


def is_prime(num):
    """ Takes num and checks if prime. True - prime | False - not prime. """
    if num < 2:
        num = False
    else:
        for i in range(2, num):
            if num % i == 0:
                num = False
                break
        else:
            num = True
    return num


def gather_input(message):
    """ Gathers user's input displaying message and stores in int(num) with error handling . """
    while True:
        try:
            choice = int(input(message))
            if choice <= 0:
                while choice <= 0:
                    choice = int(input('Cannot enter "0" or a negative number.\n'
                                       'Please enter your number: '))
            return choice
        except ValueError:
            print('Error: Invalid value, please try again!')



def play_again():
    """ Asks the user if they would like to play again. """
    string1 = 'Would you like to play again? ' + '(yes/no): '
    play_choice = input(string1)
    if play_choice.lower() == 'yes':
        return True
    else:
        return exit()


def main():
    print('Welcome to the prime number calculator...')
    play = True
    while play:
        num = gather_input('Please enter your number: ')
        num = is_prime(num)
        if num is True:
            message = 'Your number is prime!'
        else:
            message = 'Your number is not prime!'
        print(message)
        print()
        play = play_again()


#   call main when this file is run
if __name__ == '__main__':
    main()

#   Like with the preview problem, I had to really look into prime number equations and
#   what it means for a number to be prime. I then built the equation and had to test
#   multiple times prior to it being correct.