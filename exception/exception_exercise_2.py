'''
try to open file
'''

def open_file(file_name: str) -> None:
    try:
      with open('file.txt', 'r') as file:
        content = file.read() 
      return content
    except FileNotFoundError as e:
       return 'File Not Found'
    
       
print(open_file("Bollox.txt"))