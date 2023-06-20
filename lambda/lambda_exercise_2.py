'''
sort a list of tuples 
'''

def sort_list(input_list: list) -> list:
    return sorted(input_list, key=lambda item: item[1])

a_list = [(1, 3), (4, 1), (4, 2), (0, 7)]
print(sort_list(a_list))