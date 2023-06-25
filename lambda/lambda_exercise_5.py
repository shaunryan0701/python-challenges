'''
sort array by dict key
'''

def sort_array_by_key(input_list: list) -> list:
    input_list.sort(key=lambda stock: stock['price'])
    return input_list

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(sort_array_by_key(stocks))