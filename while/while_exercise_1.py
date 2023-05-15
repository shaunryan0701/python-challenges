'''
return first x prime numbers
'''

def return_first_x_prime_numbers(num_primes: int) -> list:
    prime_list = []
    num = 2
    while len(prime_list) <= num_primes:
        for i in range(2, num): 
            if num % i == 0:
                break
        else:
            prime_list.append(str(num))
        num += 1
    return prime_list

print(','.join(return_first_x_prime_numbers(100)))