'''
read stock data and calculate average
'''
def read_file(file_name: str) -> None:
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    
    closing_price = []
    for idx, line in enumerate(lines):
        if idx > 0:
            print(line)
            closing_price.append(line.split(',')[-2])
            print(closing_price)

read_file("playway.txt")