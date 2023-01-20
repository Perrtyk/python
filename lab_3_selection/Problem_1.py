# Patryk Kostek
# Lab 3 Problem 1
'''
Design and implement a program that determines if a person qualifies for a loan based on
his/her/their annual salary and length of employment at his/her/their current job.
In order to qualify a loan you must earn at least $40K per year and have worked at your
job for at least 1 year.  Your solution should have at least a main function.
'''
#
# IPO Chart:
#
# Input:
# input salary, length
#
# Processing:
# define min_income
# define min_length
# get salary, employ_length
# if salary >= min_income and employ_length >= min_length
#   then print(" Congratulations, you qualified for the loan! ")
#   else print(" I am sorry... unfortunately you do not qualify.. ")

# Output:
# message
#
# Example:
# .5 year and 30K - don't qualify
# .5 year and 50K - don't qualify
# 3 years and 30K - don't qualify
# 3 years and 50K - do qualify
#
#
# Algorithm
#    display instructions
#    get salary
#    get employ_length
#
#    if salary >= min_income and employ_length >= min_length then
#        message = str( Congratulations, you qualify! )
#    else
#        message = str( Sorry.. you don't qualify... )
#    end if
#
#    print(message)


#   gathers how much is the user's salary and their employment length
def user_input():
    """ gather user's input, return in salary, employ_length"""
    salary = float(input('What is your salary? (Ex: 40k = 40000): '))
    employ_length = float(input('How long have you been working? (40Ex: 1 year = 1): '))
    return salary, employ_length


#   processes the input to see if the user qualifies for the loan
def process(min_income, min_length):
    """ runs the process based on 'min income' income and at least 'length' years """
    salary, employ_length = user_input()
    if salary >= min_income and employ_length >= min_length:
        message = str('Congratulations you qualify!')
    else:
        message = str('Sorry... you dont you qualify!')
    return print(message)


#   prints the welcome message and runs the process which has user_input embedded
def main():
    print('Please provide us with the following information to see '
          'if you approve for our loan. ')
    process(40000, 1)


if __name__ == '__main__':
    main()

#   With this problem I found I was not very familiar with operators such as >=. I began
#   by researching examples from the book and was able to build my if statement.






