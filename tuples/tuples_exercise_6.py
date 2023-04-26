'''
sort tuple within yuple
'''

def sort_tuple_within_tuple(tup: tuple, direction = 'A') -> tuple:
    # info = (('Monica', 19), ('Tom', 21), ('John', 18))
    if direction == 'A':
      return tuple(sorted(tup, key=lambda item: item[1]))
    else:
      return tuple(sorted(tup, key=lambda item: item[1], reverse=True))