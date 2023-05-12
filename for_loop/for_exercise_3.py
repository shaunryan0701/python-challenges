'''
remove duplictes from list
'''

def remove_duplicates_rom_list(input_list: list) -> list:
    unique_items = []
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

items = [1, 5, 3, 2, 2, 4, 2, 4]
print(remove_duplicates_rom_list(items))