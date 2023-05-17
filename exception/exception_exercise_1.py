'''
divide by zero exception
'''

def divide_by_zero_exception(numerator: int, divisor: int) -> float:
    try:
        return numerator / divisor
    except ZeroDivisionError as e:
        return 'Division by zero error'

print(divide_by_zero_exception(100, 0))
