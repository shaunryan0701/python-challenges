'''
generate event numbers and save to file
'''

file = open('num.txt', 'w')

for number in range(1, 19):
    if number % 2 == 0:
        file.write(str(number) + '\n')

file.close()