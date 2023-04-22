'''
  Follow the next steps:

  1. Change all letters to lowercase.

  2. Delete spaces and period.

  3. Create a set consisting of all letters in the text and assign to letters variable

  4. Using the appropriate method for sets, remove all vowels from letters set:

    vowels = {'a', 'e', 'i', 'o', 'u'}

  5. Print the number of items in the letters set as shown below.
'''

def count_items_in_set(input_string: str) -> int:
    text = input_string.lower().replace(' ', '').replace('.', '')
    vowels = {'a', 'e', 'i', 'o', 'u'}
    letters = set(text)
    consonants = letters.difference(vowels)
    return len(consonants)
