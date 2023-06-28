'''
use generator to return list of files of a type
'''

def file_gen(file_list: list):
    for file_name in file_list:
        if file_name.endswith('.txt'):
            yield file_name


fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
print(list(file_gen(fnames)))