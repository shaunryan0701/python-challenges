'''
insert and delete from a list
'''

def add_to_list(input_list: list, insert_text: str) -> list:
    input_list.insert(0, insert_text)
    return input_list

def remove_from_list(input_list: list, remove_text: str) -> list:
    input_list.remove(remove_text)
    return input_list