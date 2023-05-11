'''
update dictionary value
'''

def check_and_udpate_dict_value(input_dict: dict, dict_value: str) -> dict:
    if dict_value in input_dict:
        input_dict[dict_value] = 'open'

    return input_dict
