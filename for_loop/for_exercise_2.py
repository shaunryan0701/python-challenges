'''
remove odd numbers form list
'''

def remove_odd_numbers_from_list(input_list: list) -> list:
    even_numbers = []
    for number in input_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

print(remove_odd_numbers_from_list(items))