'''
read stock data and calculate average
'''
def read_file(file_name: str) -> None:
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        print(lines)

read_file('playway.txt')