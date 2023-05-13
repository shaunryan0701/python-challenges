'''
compare 2 lists
'''

def compare_2_lists(list_1: list, list_2: list) -> bool:
    found_it = False
    for item in list_1:
        if item in list_2:
            found_it = True
            break
    return found_it

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
print(compare_2_lists(list1, list2))