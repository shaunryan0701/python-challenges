'''
read file into a list
'''

file = open('currencies.txt', 'r')
currency_list = [line for line in file.read().splitlines() if 'USD' in line]

print(currency_list)