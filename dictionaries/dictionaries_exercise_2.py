'''
extract dictionary values
'''

def extract_dict_values(input_dict: dict) -> list:
# capitals = {
#     'USA': 'Washington',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }

    values = []
    for value in input_dict.values():
        values.append(value)

    return values