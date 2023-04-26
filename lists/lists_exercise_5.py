'''
extend a list with an iterable (list, set, tuple, string)
'''

def extend_list(input_list: list, extension) -> list:
    input_list.extend(extension)
    return input_list