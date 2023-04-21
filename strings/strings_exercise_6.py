'''
Check for alphanumeric
'''

def check_for_alpha_numeric(check_string: str) -> bool:
    if check_string.isalnum():
        return True
    
    return False