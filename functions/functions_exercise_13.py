'''
count the number of strings in an iterable
'''

def count_strings(iterable) -> int:
    strings = []
    for item in iterable:
        if isinstance(item, str):
            strings.append(item)

    return len(strings)

iterable_1 = ['p', 2, 4.3, None]
iterable_2 = {'p', 2, 4.3, True, 'True', None}

print(count_strings(iterable_1))
print(count_strings(iterable_2))