'''
use the map function and a lamdbda to conevrt a list to the lengths of the elements
'''

def map_element_lengths(input_list: list) -> list:
    return list(map(lambda stock : len(stock), input_list))

stocks = ['playway', 'boombit', 'cd projekt']
print(map_element_lengths(stocks))