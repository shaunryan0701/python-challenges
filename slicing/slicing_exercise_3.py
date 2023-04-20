'''
Retrieve string separators and convert to binary 
'''

def convert_to_binary(input: str) -> int:
    binary_string = input[::2]
    return int(binary_string, 2)