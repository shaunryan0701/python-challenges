'''
divide one list ny another
'''

def divide_list_into(input_list_1: list, input_list_2: list) -> list:
    output_list = list(map(lambda num1, num2: num1 % num2, input_list_1, input_list_2))
    return output_list

num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]
print(divide_list_into(num1, num2))
