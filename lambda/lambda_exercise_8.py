'''
remove character fro liost items
'''

def remove_char_from_list_items(input_list: list) -> list:
    clean_list = list(map(lambda item: item.replace('-', ''), input_list))
    return clean_list

items = ['P-1', 'R-2', 'D-4', 'F-6']

print(remove_char_from_list_items(items))