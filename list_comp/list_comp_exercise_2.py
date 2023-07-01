'''
Using the list comprehension, calculate the gross price for each product. 
Round the price to two decimal places and print result to the console
'''

def calc_gross_price(items_list: list) -> list:
    gross_price = [round(item + item * 0.23, 2) for item in items_list]
    return gross_price


net_price = [5.5, 4.0, 9.0, 10.0]
print(calc_gross_price(net_price))