'''
update dictioanary value within a dictionary
'''

def update_dictionary(input_dict: dict, input_key: str, input_value: float) -> dict:
    key_to_update = list(input_dict[input_key].keys())[0]
    input_dict[input_key][key_to_update] = input_value
    return input_dict

