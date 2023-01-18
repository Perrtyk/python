'''
    Design and implement a program that asks the user to enter a US dollar amount and
    calculates the value of that dollar amount in Euros, Canadian Dollars and Mexican Pesos.
    The current exchange rates can be found on the internet.
'''

# Input
#   usd
#
# Processing
#   get usd
#   calculate usd to eur
#   calculate usd to cad
#   calculate usd to mxn
#   print usd to all conversion
#
# Output
#   usd input
#   usd to eur
#   usd to cad
#   usd to mxn

# Example
#   usd to eur = usd * 0.93
#   usd to cad = usd * 1.26
#   usd to mxn = usd * 18.93

#   defining the current value of eur, cad, mxn
eur = float(0.93)
cad = float(1.26)
mxn = float(18.93)

#   display the welcome message and prompt for input from user
print('Welcome to the USD to Euro, Canadian Dollar and Mexican Peso converter!')
print('Please input the dollar amount you wish to convert (ex: 153.50): ')
usd = float(input('USD: '))

#   convert the usd variable to eur, cad, mxn
eur = str(round(usd * eur, 2))
cad = str(round(usd * cad, 2))
mxn = str(round(usd * mxn, 2))

#   convert usd to str
usd = str(round(usd, 2))

#   display the conversion rates
print(usd + ' USD is worth:')
print()
print(eur + ' Euros.')
print(cad + ' Canadian Dollars.')
print(mxn + ' Mexican Pesos.')

