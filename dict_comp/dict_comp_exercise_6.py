'''
combine keys and values into a dictionary
'''

def combine_keys_and_values(key_list: list, value_list: list) -> dict:
    dictionary = {index: {property: None for property in value_list} for index in key_list}
    return dictionary

indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['number of companies', 'companies', 'cap']

print(combine_keys_and_values(indeks, properties))