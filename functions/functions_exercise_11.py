'''
filter list by length
'''

def filter_list_by_length(input_list: list) -> list:
    filter_list = []
    for item in input_list:
        if len(item) >= 6:
            filter_list.append(item)

    return filter_list

list_of_items = ['programming', 'python', 'java', 'sql']

print(filter_list_by_length(list_of_items))
print(filter_list_by_length(['java', 'sql']))