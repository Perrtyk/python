'''
    Design and implement a program that can be used by 2nd grade students to practice addition of up
    to 3 digit numbers.  The program should generate 2 random integers between 10 and 999 and display
    the 2 numbers to the user.  The user should be allowed to enter his/her/their answer to the
    addition problem.   The program should tell the user when his/her/their answer is correct and
    should display the correct answer when the answer is incorrect.  You may edit your solution to
    the problem from lab 1.   Your solution should have a function called checkResult as well as a
    main function.  checkResult should have 3 parameters, the first and second random number as well
    as the user's answer.  checkResult should check the user's answer and display an appropriate
    message.  main should generate the random numbers, display the problem to the user and get
    the user's answer before calling checkResult.
'''
# Patryk Kostek
# Lab 3 Problem 3
#
#
'''
Input
  user_ans
Processing
    import random library
    define num1 and num2 as random numbers
    display the problem to the user
    gather input and use in check_result
    if correct:
        message is correct statement
    else:
        message is wrong statement
Output
	message

Example
  100 + 200 = 305   should print 'That is incorrect. The answer is 300!'
  100 + 200 = 300   should print 'That is correct!'

Algorithm

  process
    assign min, max variables
    assign num1 and num2 random number
    return num1 and num2 for later use
  end process
  
  gather_input
    display 'num1 + num2 = '
    prompt user for input to variable user_ans
    define variable user_ans
    return user_ans for later use
  end gather_input
  
  check_result(num1, num2, user_ans)
    if user_ans is num1 + num2
        assign message correct statement
    else
        assign message incorrect statement
        return message for later use
  end check_result
    
  
'''
import random

def rand_num(min, max):
    """ assigns initial random numbers with minimum and maximum values """
    num1, num2 = random.randint(min, max), random.randint(min, max)
    return num1, num2


def gather_input(num1, num2):
    """ prints math question and prompts user for input, stores in user_ans """
    user_ans = input(f'{num1:3} + {num2:3} = ')
    return user_ans


def check_result(num1, num2, user_ans):
    """ validates whether the user's input matches the database answer, assigns message """
    if user_ans == (num1 + num2):
        message = 'You are correct!'
    else:
        message = 'You are incorrect! The correct answer is ' + str(num1 + num2) + '.'
    return message

def main():
    """ runs main code, alter number range in randum_num function here """
    num1, num2, = rand_num(10, 999)
    user_ans = gather_input(num1, num2)
    message =  check_result(num1, num2, user_ans)
    print(message)


main()