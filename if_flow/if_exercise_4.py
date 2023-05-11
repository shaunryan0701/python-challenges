'''
check if item in list and add
'''

def check_if_item_in_list(input_list: list, input_item: str) -> list:
    if input_item not in input_list:
        input_list.append(input_item)

    return input_list

project_ids = ['02134', '24253']
project_id = '24253'

print(check_if_item_in_list(project_ids, project_id))