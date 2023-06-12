'''
find the length of the longest word
'''

def find_longest(input_list: list) -> int:
    lengths = []
    for word in input_list:
        lengths.append(len(word))

    return max(lengths)

print(find_longest(['java', 'sql', 'r']))