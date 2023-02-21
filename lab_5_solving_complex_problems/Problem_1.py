# Patryk Kostek
# Lab 5 Problem 1
#
'''

Design and implement a program that can be used to provide users with information about the
monthly payment for a car loan.  The program should allow a user to enter the amount of the
loan and the annual interest rate.  The program should validate data entered by the user
in a reasonable way and should force the user to reenter until the data is correct.  The
program should display the monthly payment for a 4 year loan, a 5 year loan and a 6 year
loan in an attractively formatted table.  The formula for calculating the payment is:
payment = (monthly rate * loan amount) / ( 1- (1 + monthly rate) ^ - number of months).

Algorithm:

welcome
    define message with welcome message
    print message
end welcome

getinfo
    While True
        try
            loan_amount defined by user input
            if loan_amount negative
                print error statement
            else
                continue
        except for value error
            print error statement
    While True
        try
            int_rate defined by user input
            if int_rate negative
                print error statement
            else
                continue
        except for value error
            print error statement
    return loan_amount and int_rate rounded
end get_info

    intRate defined by user input


'''


def welcome():
    message = 'Welcome to the "Car Loan Calculator", please input your information below.'
    print(f'{message:^{120}}')


def get_info():
    """ Gathers the users loan and interest information and returns the information. """
    # defining variables and error text for later use in error handling
    loan_message = 'Loan Amount: $'
    rate_message = 'Interest % : '
    ERROR = '\033[91mERROR\033[0m:'
    # defining table strings and bold start/end of strings
    start_bold, end_bold = ('\033[1m', '\033[0m')

    # while loop for gathering loan amount
    while True:
        try:
            loan_amount = float(input(loan_message))
            if loan_amount <= 0:
                print(f'{ERROR} The value is negative or zero. Please enter a positive value.')
            else:
                break
        except ValueError:
            print(f'{ERROR} Invalid value! Please enter a correct value.')

    # while loop for gathering interest rate amount
    while True:
        try:
            int_rate = float(input(rate_message))
            if int_rate <= 0:
                print(f'{ERROR} The value is negative or zero. Please enter a positive value.')
            elif int_rate > 100:
                print(f'{ERROR} The value is too large! Please enter a percentage. '
                      f' (We are not that greedy...)')
            else:
                break
        except ValueError:
            print(f'{ERROR} Invalid value! Please enter a correct value.')
    # prints the users requested data for the loan information, rounding the number
    total_string = f'{start_bold}Loan Amount Requested:{end_bold} ${loan_amount:.2f}' + ' ' * 6 + \
                   f'{start_bold}Interest Rate Requested:{end_bold} {int_rate:.2f}%'
    print(f'{total_string:^{135}}')
    # returning the loan_amount and int_rate values for later use
    return round(loan_amount, 2), (int_rate * 0.01)


def get_payment(loan_amount, int_rate):
    """ Processes the user's input to see if their payment options. """
    # building list for months per years 4, 5 and 6
    months = [48, 60, 72]
    # building empty payments list for appending
    payments = []
    # runs payment formula for each object in list above
    for month in months:
        payment = round((int_rate * loan_amount) / (1 - (1 + int_rate) ** (-1 * month)), 2)
        payments.append(payment)
    # returns the now full payment list
    return payments


def print_table(payment_list):
    """ Prints the table with the final information using a list. """
    # defining table strings and bold start/end of strings
    start_bold, end_bold = ('\033[1m', '\033[0m')
    final_string = 'According to your data, these are your payment options.'
    header = f'Loan Time   Monthly Payment'
    line2 = f'4 Year    | {payment_list[0]:.2f}'
    line3 = f'5 Year    | {payment_list[1]:.2f}'
    line4 = f'6 Year    | {payment_list[2]:.2f}'
    # print the final table
    print(f'{start_bold}{header:>76}{end_bold}')
    print(f'{line2:>67}')
    print(f'{line3:>67}')
    print(f'{line4:>67}')
    print()
    print(f'{final_string:^{120}}')


def main1():
    welcome()
    while True:
        user_loan, user_interest = get_info()
        monthly_payments = get_payment(user_loan, user_interest)
        print_table(monthly_payments)
        play_again = input('Would you like to request another loan?: ')
        if play_again.lower() != 'yes':
            break
    return print('Thank you for shopping!')


#   call main when this file is run
if __name__ == '__main__':
    main1()
