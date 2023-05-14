'''
convert closing price
'''

def convert_closing_price(input_dict: dict) -> dict:
    for key, value in input_dict.items():
        if value[1] == 'PLN':
            continue
        value[0] = value[0] * 4
        value[1] = 'PLN'

    return input_dict

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

print(convert_closing_price(gaming))