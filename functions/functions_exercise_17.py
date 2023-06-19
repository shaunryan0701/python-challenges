'''
check if a string is a palindrome
'''

def check_palindrome(input_string: str) -> bool:
   inverse = input_string[::-1] 
   if inverse == input_string:
      return True
   else:
      return False
   
print(check_palindrome('poopoop'))
print(check_palindrome('bollox'))