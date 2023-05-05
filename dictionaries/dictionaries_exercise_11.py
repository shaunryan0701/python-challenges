'''
delete from key value pair from  dictionary
'''

def delete_from_dict(input_dict: dict, delete_key: str) -> dict:
    input_dict.pop(delete_key)
    return input_dict


