'''
get dictioanry values by key
'''

def get_dictionary_values_by_key(input_dict: dict, input_key: str):
  #   stocks = {
  #   'MSFT.US': {'Microsoft Corp': 184},
  #   'AAPL.US': {'Apple Inc': 310},
  #   'MMM.US': {'3M Co': 148}
  # }
  stocks = input_dict[input_key]
  price = 0
  for stock in stocks.values():
    price = stock

  return price
