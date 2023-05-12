'''
split string and return first 4 words
'''

def split_string(input_string: str) -> list:
    word_list = input_string.lower().split(sep=' ')
    return word_list[:4]

text = 'Python is a very popular programming language'
print(split_string(text))