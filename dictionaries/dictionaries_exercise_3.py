'''
extract dictionary items
'''

def extract_dict_items(input_dict: dict) -> list:
# capitals = {
#     'USA': 'Washington',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }

    items = []
    for item in input_dict.items():
        items.append(item)


    return items