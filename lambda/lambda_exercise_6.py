'''
filter list by dictionary key
'''

def filter_list_by_key(input_list: list) -> list:
    filtered_list = list(filter(lambda stock: stock['index'] == 'mWIG40', input_list))
    return filtered_list

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(filter_list_by_key(stocks))