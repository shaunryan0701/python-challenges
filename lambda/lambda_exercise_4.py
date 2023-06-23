'''
sort list by sum of squaress
'''

def sort_list(input_list: list):
  input_list.sort(key = lambda pair: pair[0]**2 + pair[1]**2)
  return input_list

items = [(3, 4), (2, 5), (1, 4), (6, 1)]
print(sort_list(items))

x = 3
y = 2
z = 3
 
def my_func(x,y,z=1):
    return(x**y**z)

print(list(range(0, 10)))