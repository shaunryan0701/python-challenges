'''
From the text list delete all newline characters. Then delete empty lines and print the text to the console.
'''

def read_file():
  with open('gaming.txt','r') as file:
      text = file.readlines()
  print(text)
  clean_list = [line.replace('\n', '') for line in text if line != '\n']
  print(clean_list)
        
read_file()