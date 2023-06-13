'''
calulate the factorial of a given number
'''

def calculate_factorial(input_num: int) -> int:
    if input_num == 0:
        return 1
    return input_num * calculate_factorial(input_num - 1)

print(calculate_factorial(10))