'''
read stock data and calculate average
'''
def read_file(file_name: str) -> float:
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    
    closing_price = []
    for idx, line in enumerate(lines):
        if idx > 0:
            print(line)
            closing_price.append(int(line.split(',')[-2]))

    print(closing_price)
    closing_average = sum(closing_price) / len(closing_price)
    return closing_average

print(f'3-day average closing price: {round(read_file("playway.txt"), 2)}')