'''
check if list contains distinct values
'''

def is_distinct(input_list: list) -> bool:
    return len(set(input_list)) == len(input_list)
    

print(is_distinct([1,2,3]))
print(is_distinct([1,2,2,3,3]))