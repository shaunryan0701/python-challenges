'''
find the number of unique words in a string
'''

def count_unique_words(input_string: str) -> int:
    word_list = input_string.replace(',', '').replace(':', '').replace('.', '').split()
    unique_words = {word for word in word_list}
    return unique_words

desc = "Playway: Playway is a producer of computer games."

print(len(count_unique_words(desc)))