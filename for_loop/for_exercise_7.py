'''
search through list for matching string
'''

def search_list_for_string_match(input_list: list, search_string_list: list) -> list:
    all_matches = []
    for search_string in search_string_list:
      matches = [item for item in input_list if search_string in item]

      all_matches += matches

    return all_matches

indexes = [
    'BOVESPA',
    'DOW JONES COMP',
    'DOW JONES INDU',
    'DOW JONES TRANS',
    'DOW JONES UTIL',
    'IPC',
    'IPSA',
    'MERVAL',
    'NASDAQ COMP',
    'NASDAQ100',
    'S&P500',
    'S&P/TSX COMP',
]

search_strings = ['DOW', 'S&P']

print(search_list_for_string_match(indexes, search_strings))