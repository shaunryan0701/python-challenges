'''
save text to jsom
'''

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    file.write(str(stocks))