'''
extract from list into tuple
'''

def extract_from_list_to_tuple(input_list: list) -> list:
    tuple_list = []
    idx = 0
    for input  in input_list:
        tuple_list.append((idx, input))
        idx += 1

    # return tuple_list 
    return list(enumerate(input_list))  

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

print(extract_from_list_to_tuple(tickers))