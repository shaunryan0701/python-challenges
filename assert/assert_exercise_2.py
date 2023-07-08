'''
By using the assert statement inside this function, 
add the ability to check the length of the numbers argument before returning the result
'''

def max_min_diff(numbers):
    assert len(numbers) > 0, 'The numbers object cannot be empty.'
    return max(numbers) - min(numbers)

# print(max_min_diff([23, 11]))

if __name__ == '__main__':
    print(max_min_diff([]))