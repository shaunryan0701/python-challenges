'''
Using dict comprehension, extract a key: value pair from the dictionary 
with a value greater than 100 and print the result to the console
'''

def extract_stocks(input_dict: dict) -> dict:
    stocks_gt_100 = {key: value for key, value in input_dict.items() if value > 100} 
    return stocks_gt_100

stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
print(extract_stocks(stocks))