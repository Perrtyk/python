# Patryk Kostek
# Lab 1 Problem 1
''' Design and implement a program that asks the user to enter a
    temperature in degrees Fahrenheit, calculates and displays the
		same temperature in degrees celsius. c = 5/9 * (f - 32).
'''
# Input
#   tempF - whole number
# Processing
#   get tempF
#   calculate tempC
#   display tempC
# Output
#   tempC - real number

# Example
#   212 f is 100 C
#   5/9 * (212 - 32) = 5/9 * 180 = 100

# state input from user.
print('Enter the temperature in degrees fahrenheit to convert to celsius: ')
# require input for tempF from user.
tempF = int(input('Degrees in Fahrenheit: '))
# calculate tempC from tempF input.
tempC = 5 / 9 * (tempF - 32)
# print output in celsius.
print()
print(str(tempF) + ' Degrees Fahrenheit is ' + str(round(tempC, 2)) + ' degrees celsius.')

# Initially I made a line to change TempF into an integer after the user's input
# I later fixed this by making the input itself an integer, saving a line in the code.

