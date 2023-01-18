''' Design and implement a program that can be used with elementary
    school children to teach about change.  The program should ask the student to enter a price that is less than 1 dollar.  The program will calculate and display the amount of change due as well as the number of quarters, dimes, nickels and pennies.
'''

# Input
#   price
# Processing
#   get price
#   calculate change
#   calculate quarters
#   calculate dimes
#   calculate nick
#
# Output
#   change
#   quarters
#   dimes
#   nickels
#   pennies

# Example
#   price = 34
#   change = 100 – 34 = 66
#   quarters = 66/25 = 2
#   change = 66 – 2 * 25 = 16

print('Please enter a price that is less than 1 dollar and see'
      ' how much change you have! (100 = 1 dollar.)')
# gather input for price
price = input()
# define change left over after price
change = 100 - int(price)

# how many quarters are given out from the change
quarters = int(int(change) / 25)
# alter change variable after quarters given out
change = int(change) - int(quarters) * 25

# how many dimes are given out from the change
dimes = int(int(change) / 10)
# alter change variable after dimes given out
change = int(change) - int(dimes) * 10

# how many nickles are given out from the change
nickles = int(int(change) / 5)
# alter change variable after nickles given out
change = int(change) - int(nickles) * 5

# how many pennies are given out from the change
pennies = int(int(change) / 1)
# alter change variable pennies dimes given out
change = int(change) - int(pennies) * 1

# state the final change left over after the purchase in coins and total
print('You have a total of: '
      + str(quarters) + ' quarter(s), '
      + str(dimes) + ' dime(s), '
      + str(nickles) + ' nickle(s), '
      + 'and ' + str(pennies) + ' pennie(s). ')

change = 100 - int(price)
print('Totaling: ' + str(change) + ' cents.')


