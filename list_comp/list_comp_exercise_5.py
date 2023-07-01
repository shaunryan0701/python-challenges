'''
1. Get rid of blank lines.
2. Split each line into tokens/words as shown below and print result to the console.
'''

def clean_and_split_lines() -> list:
    with open('plw.txt', 'r') as file:
      lines = file.read().splitlines()

    word_list = [line.split() for line in lines if len(line) > 0]
    print(word_list)

clean_and_split_lines()