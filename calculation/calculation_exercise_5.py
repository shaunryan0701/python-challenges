def geometric_sequence(n: int):
    return 8 * (2 ** (n - 1))
    
def sum_geometric_sequence(n: int):
    sum = 0 
    for num in range(1, n+1):
        sum += geometric_sequence(num)
    return sum