'''
Standard deviation
((x1 - mean **2 + x2 - mean **2 + x3 - mean **2) / len(x)) ** 1/2
'''
import math

def standard_deviation(sample: list) -> float:
    sample_size = len(sample)
    mean = sum(sample) / sample_size

    total = 0
    for x in sample:
        total += (x - mean) ** 2

    return round((total / sample_size) ** (1/2), 2)