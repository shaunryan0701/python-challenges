'''
create a list of words from text
'''

def create_word_list_from_text(input_text: str) -> list:
    word_list = input_text.replace('\n', ' ').replace('.', '').lower().split(sep=' ')
    longer_words = []

    longer_words = [word for word in word_list if len(word) > 6]

    return longer_words


text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

print(create_word_list_from_text(text))