'''
Convert dictionary into the following list and print the result to the console
'''

def convert_dict_to_list(input_dict: dict) -> list:
    zip_list = [[x, y] for x, y in input_dict.items()]
    print(zip_list)

data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
print(data)
convert_dict_to_list(data)