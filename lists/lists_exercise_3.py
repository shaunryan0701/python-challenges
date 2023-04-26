'''
unique characters
Standardize the text (replace uppercase letters with lowercase). 
Then create a list of unique characters in the text. 
Remove the space from this list and sort from a to z. 
'''

def unique_chars(text: str) -> int:
    unique_chars = []
    text = text.lower().replace(' ', '')

    # can load the text into a list via a set() which does not allow duplicates
    # converting direct to a list allows duplicates
    # unique_chars = list(set(text))
    for char in text:
        if char not in unique_chars:
          unique_chars.append(char)
    
    unique_chars.sort()
    return unique_chars
