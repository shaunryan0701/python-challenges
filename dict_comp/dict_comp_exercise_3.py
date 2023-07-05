'''
Use dict comprehension to replace values with keys and print the result to the console
'''

def replace_values_with_keys(input_dict: dict) -> dict:
    swapped_dict = {value: key for key, value in input_dict.items()}
    return swapped_dict

stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
print(replace_values_with_keys(stocks))