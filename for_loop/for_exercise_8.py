'''
iterate through dictionary for values meeting criteria
'''

def find_values_in_dict(input_dict: dict, search_value: float) -> list:
    key_list = [key for key, value in input_dict.items() if value > search_value]

    return key_list

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

print(find_values_in_dict(gaming, 100.0))
        