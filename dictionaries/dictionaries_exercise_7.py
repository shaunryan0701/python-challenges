'''
append dictionary item
'''

def add_dictionary_item(input_dict: dict, input_key: str, input_name: str, input_value: float) -> dict:
    item = {input_name : input_value}
    input_dict[input_key]= item
    return input_dict

