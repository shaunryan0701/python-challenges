'''
sort a tuple
'''
def sort_tuple(tup: tuple, direction: str) -> tuple:
    # sorted() returns a list
    if direction == 'A':
      return tuple(sorted(tup))
    else:
      return tuple(sorted(tup, reverse=True))