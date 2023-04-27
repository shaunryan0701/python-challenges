'''
extract dictionary keys
'''

def extract_dict_keys(input_dict: dict) -> list:
# capitals = {
#     'USA': 'Washington',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }

    keys = []
    for key in input_dict.keys():
        keys.append(key)

    return keys

