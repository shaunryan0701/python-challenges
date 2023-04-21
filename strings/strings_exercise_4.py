'''
Check string contains
'''

def check_string(input_string: str, check_string: str) -> bool:
    if input_string.startswith(check_string):
        return True
    
    return False