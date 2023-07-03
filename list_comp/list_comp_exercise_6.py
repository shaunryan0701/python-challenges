'''
1. Change uppercase letters to lowercase
2. Remove commas and periods
3. Split the text into tokens
4. Extract words with minimum 8 characters length
5. Sort the words alphabetically
Print the result to the console.
'''

def extract_words_from_list() -> list:
    with open('plw.txt', 'r') as file:
      lines = file.read()

    lines = lines.lower().replace(',', '').replace('.', '')
    word_list = lines.split()

    words_gt_8 = [word for word in word_list if len(word) >= 8]
    words_gt_8.sort()
    print(words_gt_8)

extract_words_from_list()