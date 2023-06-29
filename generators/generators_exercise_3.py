'''

'''

def dayname(index, input_list):
    index = index % 7
    yield input_list[index - 1]
    yield input_list[index]
    yield input_list[index + 1]


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for pair in dayname(0, days):
    print(dayname(0, days))