'''
Using the json package, dump a dictionary
'''
import json

def dump_dictionary(input_dict: dict):
    return json.dumps(input_dict, sort_keys=True, indent=4)


stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
print(dump_dictionary(stocks))