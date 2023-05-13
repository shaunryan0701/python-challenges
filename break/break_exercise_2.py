'''
check element type in list
'''

def check_element_type(input_list: list) -> bool:
    is_string = True
    for item in input_list:
        if not isinstance(item, str):
            is_string = False
            break
        
    return is_string

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

print(check_element_type(hashtags))