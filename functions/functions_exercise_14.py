'''
remove duplicates from a list
'''

def remove_duplicates(input_list: list) -> list:
    deduped_list = []
    for item in input_list:
        if item not in deduped_list:
            deduped_list.append(item)

    # return deduped_list
    # or
    return list(set(input_list))


print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
print(remove_duplicates([1, 1, 1, 1]))