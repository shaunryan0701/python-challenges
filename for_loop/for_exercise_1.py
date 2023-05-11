'''
find all 2 digit numbers divisable by 11
'''

def all_2_digit_numbers_divisable_by_11() -> str:
    number_list = []
    for number in range(10, 100):
        if number % 11 == 0:
            number_list.append(str(number))
    
    return ','.join(number_list)
