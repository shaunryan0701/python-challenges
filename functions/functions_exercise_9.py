'''
find the product of an iterable
'''

def product_iterable(input_nums) -> int:
    product = 1
    for number in input_nums:
        product *= number 

    return product

print(product_iterable((1,2,3,4)))

print(product_iterable([1,2,3,4]))

print(product_iterable([4, 2, -5]))
