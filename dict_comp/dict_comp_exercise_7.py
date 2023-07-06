'''
convert ist to a dictionary
'''

def convert_list_to_dict(input_list: list) -> dict:
    output_dict = dict(enumerate(input_list))
    return output_dict


indexes = ['WIG20', 'mWIG40', 'sWIG80']
print(convert_list_to_dict(indexes))