'''
Using dict comprehension, create a dictionary that maps the numbers 
1 to 7 into squares and print the result to the console.
'''

def map_numbers_to_squares() -> dict:
    squares = {num: num**2 for num in range(1,8)}
    print(squares)

map_numbers_to_squares()