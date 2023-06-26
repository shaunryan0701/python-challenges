'''
convert list to boolean list
'''

def convert_list_to_boolean_list(input_list: list) -> list:
    bool_List = list(map(lambda stock: stock['index'] == 'mWIG40', input_list))
    return bool_List
    

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(convert_list_to_boolean_list(stocks))