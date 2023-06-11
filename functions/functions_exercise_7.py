'''
count the number of ones in a binary number
'''

def count_ones(input_num:int) -> int:
    binary_num = bin(input_num)[2:]
    return binary_num.count('1')

print(count_ones(234))