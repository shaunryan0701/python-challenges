'''
convert list to histogram
'''

def convert_list_to_histogram(input_list: list) -> dict:
    histogram = {}
    for item in input_list:
        if item not in histogram.keys():
            histogram[item] = 1
        else:
            histogram[item] += 1

    return histogram

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
print(convert_list_to_histogram(input_list=items))