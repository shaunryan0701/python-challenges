'''
extract unique values from list
'''

def extract_unique_items(input_dictionary: dict) -> list:
    result = list(set(input_dictionary.values()))
    result.sort()
    return result 
