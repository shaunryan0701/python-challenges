'''
Use dict comprehension to build a dictionary that maps company names 
to the number of characters of its name and print the result to the console
'''

def build_dict_with_key_length(input_list: list) -> dict:
    stock_dict = {item: len(item) for item in input_list}
    return stock_dict

stocks = ['Playway', 'CD Projekt', 'Boombit']
print(build_dict_with_key_length(stocks))