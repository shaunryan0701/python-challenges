'''
Find the max of 3 numbers
'''

def find_max(num1: int, num2: int, num3: int) -> int:
    num_list = [num1, num2, num3]
    return max(num_list)


print(find_max(99, 999, 9999))