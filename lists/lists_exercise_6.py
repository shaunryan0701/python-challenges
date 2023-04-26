'''
sort a tuple
'''

def sort_tuple(input_tuple: tuple) -> tuple:
    # sorted() function takes an iterable and returns a list
    sorted_tuple = tuple(sorted(input_tuple))
    return sorted_tuple