'''
extract from list into dictionary
'''

def extract_from_list_to_dict(input_list: list) -> dict:

    return dict(enumerate(input_list))  

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

print(extract_from_list_to_dict(tickers))