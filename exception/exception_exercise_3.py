'''
key error
'''

def search_for_key(input_dict: dict, input_key: str) -> dict:
    try:
        return input_dict[input_key]
    except KeyError as e:
        print(f'The {input_key} key is not in the dictionary. Adding key ...')
        input_dict[input_key] = None
    return input_dict

users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}    
print(search_for_key(users, '005'))