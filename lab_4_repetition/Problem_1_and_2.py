# Patryk Kostek
# Lab 4 Problem 1 and 2
#
"""
    Design and implement a program that asks the user to enter a number and determines if
    the number entered is a perfect number.  A perfect number is a number that is equal to
    the sum of its factors excluding the number itself.  6 is a perfect number because
    1 + 2 + 3 = 6. 28 is the next perfect number.  Your solution should include a "fruitful"
    function called isPerfect as well as a main function.  isPerfect should have one integer
    parameter, number and should return either True or False. main should get the number
    from the user, call isPerfect and display an appropriate message on the screen.

Example
  6 is perfect.  1 + 2 + 3 = 6
  8 is not perfect. 1 + 2 + 4 = 7

Algorithm - no functions
  display instructions
  get number
  sum = 0
  # need the perfect logic here

Algorithm - with functions
  isPerfect(number)
    sum = 1
    for each divisor between 2 and up to but not including the number
        if number % divisor = 0 then
            sum = sum + divisor
        end if
    end for
    if sum = number then
        return true
    else
        return false
    end if


  main (problem 1)
    display instructions
    get number
    perfect = isPerfect(number)
    if perfect = true then
        display number is isPerfect
    else
        display number is NOT isPerfect
    end if
  end main


  main (problem 2)
    display instructions
    for each number between 2 and up to but not including 1001
        perfect = isPerfect(number)
        if perfect = true then
            print number
        end if
    end for
  end main

"""


def isPerfect(number):
    """ Fruitful function that determines if number is perfect . """
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum = sum + divisor

    if sum == number:
        return True
    else:
        return False


def main1():
    """ Repetition Lab.  Problem 1. """
    number = int(input("Please enter a number: "))
    perfect = isPerfect(number)
    print(f"Is {number} perfect? {perfect}")


def main2():
    """ Repetition Lab.  Problem 2. """
    for number in range(2, 1001):
        perfect = isPerfect(number)
        if perfect == True:
            print(f'{number} is perfect')


if __name__ == '__main__':
    main2()

#   The main issues with this problem that I had is the math surrounding a perfect number.
#   I did have to do some review in order to understand the order of operations for my code.
#   It also threw me off and was awesome to learn the initializing variable technique used
#   in sum. Before calling sum, sum = 0.