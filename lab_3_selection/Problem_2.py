# Patryk Kostek
# Lab 3 Problem 2
#
'''
    Design and implement a program that implements a calculator.  The program should ask
    the user to enter 2 integer
    values as well as one of 6 arithmetic operators (+, -, *, /, //, %).  The program should
    display the arithmetic operation as well as the result.  When the user enters an arithmetic
    operator that is not one of the 6 valid operators, the program should display an
    appropriate error message rather than the results of the calculation.  Your solution
    should have a function called calculator as well as a main function.  calculator should 3
    parameters, the 2 integer values as well as the arithmetic operator.  calculator should
    display the arithmetic expression as well as the result.  main should get the input from
    the user and then call the calculator function, provided that the input is valid.

IPO Chart:
Input
    number1, number2, operator
Processing
    get number1
    get number2
    get operator
    determine if operator is valid
    do calculation
Output
    calculation and result
Example
    3 2 + should print 3 + 2 is 5
    3 2 & should print an error message

Algorithm:
    calculator (number1, number2, operator)
        if operator is +
            display number1 + number 2 is (number1 + number2)
        else if operator is -
            display number1 - number 2 is (number1 - number2)
        else if operator is *
             display number1 * number 2 is (number1 * number2)
        else if operator is /
             display number1 / number 2 is (number1 / number2)
        else if operator is //
             display number1 // number 2 is (number1 // number2)
        else if operator is %
             display number1 % number 2 is (number1 % number2)
        else
            display error message
        end if
  end calculator

    main
        display instructions
        get number1
        get number2
        get operator
        calculator (number1, number2, operator)
    end main
'''


#   uses number1, number2 and operator to calculate the answer
def calculator(number1, number2, operator):
    '''Acts as a simple calculator.  Takes 2 operands and an arithmetic operator as parameters.  Displays the result.'''
    if operator == '+':
        print(f"{number1} + {number2} = {(number1 + number2)}")
    elif operator == '-':
        print(f"{number1} - {number2} = {(number1 - number2)}")
    elif operator == '*':
        print(f"{number1} * {number2} = {(number1 * number2)}")
    elif operator == '/':
        print(f"{number1} / {number2} = {(number1 / number2)}")
    elif operator == '//':
        print(f"{number1} // {number2} = {(number1 // number2)}")
    elif operator == '%':
        print(f"{number1} % {number2} = {(number1 % number2)}")
    else:
        print('Error, invalid operator.')


#   gathers input from the user and uses the calculator(x, y, z) function
def main():
    """ prints welcome statement and gather input, uses calculator(x, y, z) """
    print('This program is a simple calculator.  The valid operators are +, -, *, /, //, %')
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    operator = input("Please enter the arithmetic operator: ")
# calls the function calculator passing the numbers and the operator as parameters
    calculator(number1, number2, operator)


# call main when this file is run
if __name__ == '__main__':
    main()

#   With this problem, I began to get comfortable with the if, elif and else statements.
#   It took some trial and error, but I was able to get the calculator function working
#   as well as the error handling.