'''
prime number checker
'''

def check_prime_number(input_number: int) -> str:
    is_prime = True
    for num in range(2, input_number):
        if input_number % num == 0: 
            is_prime = False
            break
        
    if is_prime == True:
        return str(input_number) + ' - prime number'
    else:
        return str(input_number) + ' - not a prime number'
    
print(check_prime_number(1))