'''
check file extension
'''

def check_file_extension(file_name: str, file_extension: str) -> bool:
    if file_name.endswith(file_extension):
        return True
    else:
        return False