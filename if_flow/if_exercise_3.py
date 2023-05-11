'''
check instance is int
'''

def check_is_int(input_num) -> str:
    if isinstance(input_num, int):
        return 'YES'
    else:
        return 'NO'