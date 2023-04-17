def arithmetic_sequence(n: int):
    return 10 + (4 * n)

def sum_arithmetic_sequence(n: int):
    sum = 0
    for number in range(1, n+1):
        sum += arithmetic_sequence(number)

    return sum