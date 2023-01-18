''' Design and implement a program that can be used by 2nd grade students to practice
    addition of up to 2 digit numbers.  (Yes, that means that the answer will sometimes
    be a 3 digit number!).  The program should generate 2 random integers between 10 and
    99 and display the 2 numbers to the user.  The user should be allowed to enter
    his/her/their answer to the addition problem and then program should display
    the correct answer.
'''

# Input
#   ans1
#
# Processing
#   import random library
#   define min and max variable for random int generation
#   generate num1
#   generate num2
#   add num and num 2, define ans2
#   print welcome statement
#   prompt user for input for answer problem with num1 + num2
#   print correct answer
#
# Output
#   print ans2

#   import the random int function
import random
#   defining the minimum and maximum values of the random integers
min = 10
max = 99
#   random number generation and defining variable
num1 = random.randint(min, max)
num2 = random.randint(min, max)
#   add the two random numbers into variable ans2
ans2 = num1 + num2
#   print welcome statement for the student
print('Welcome to addition problem practice! Please answer the following question:')
#   print math problem for the student
ans1 = input(str(num1) + ' + ' + str(num2) + ' = ')
#   print correct answer
print('The correct answer is: ' + str(ans2))
