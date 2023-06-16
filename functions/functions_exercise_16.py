'''
args and kwargs
'''

def function(*args, **kwargs):
    print(args, kwargs)

function(3, 4)
function(x=8, p=898)
function(1, 2, h=66, i= 88)