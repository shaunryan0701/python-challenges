'''
extract dictionary values by key
'''

def extract_dict_items_by_key(input_dict: dict, key_string: str) -> str:
    # capitals = {
    #     'USA': 'Washington',
    #     'Germany': 'Berlin',
    #     'Austria': 'Vienna'
    # }

    return input_dict.get(key_string)