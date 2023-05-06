'''
find dictionary item by key
'''

def find_dict_item_by_key(input_dict: dict, input_key: str) -> str:
    value = input_dict.get(input_key, 'indefinite')
    return value
